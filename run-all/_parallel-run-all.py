#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import sys
import os
import io
import time
import traceback
import contextlib
import re
import logging
import subprocess
import runpy
import multiprocessing as mp
from contextlib import redirect_stdout, redirect_stderr
from concurrent.futures import ProcessPoolExecutor

#logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logging.basicConfig(stream=sys.stderr, level=logging.WARN)


def natural_sort_key(s):
    """Generate a sort key that sorts strings in human/natural order."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def get_self_parent_dir():
    """Get the parent directory of the one containing the current script"""
    script_dir = os.path.dirname(os.path.realpath(__file__))
    logging.debug(f"script_dir=({script_dir})")
    parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
    logging.debug(f"parent_dir=({parent_dir})")
    return parent_dir

def get_scriptnames(path_dir):
    regex = re.compile(r'^[0-9].*\.py$')
    filenames = [
        f for f in os.listdir(path_dir)
        if os.path.isfile(os.path.join(path_dir, f)) and regex.match(f)
    ]
    filenames.sort(key=natural_sort_key)
    logging.debug(f"len(filenames)=({len(filenames)})")
    #logging.debug(f"filenames=({filenames})")
    return filenames



def _exec_script(path_script: str):
    """
    Created by ChatGPT5.2 and effectively untested 
    Executes a Python file in an isolated process, capturing stdout/stderr.
    returncode: 0 on success, 1 on exception.
    Executes a Python file in an isolated process, capturing stdout/stderr.
    Runs with the script's directory as the current working directory.
    """
    path_script = os.path.abspath(path_script)
    script_dir = os.path.dirname(path_script)

    basename_script = os.path.basename(path_script)
    print(basename_script)

    out = io.StringIO()
    err = io.StringIO()
    rc = 0

    old_cwd = os.getcwd()
    old_syspath0 = sys.path[0] if sys.path else None

    try:
        # Behave like: (cd script_dir && python script.py)
        os.chdir(script_dir)

        # Helps relative imports like `import helper` where helper.py is alongside the script.
        if sys.path:
            sys.path[0] = script_dir
        else:
            sys.path.insert(0, script_dir)

        with redirect_stdout(out), redirect_stderr(err):
            runpy.run_path(path_script, run_name="__main__")

    except SystemExit as e:
        rc = int(e.code) if isinstance(e.code, int) else 0
    except Exception:
        rc = 1
        err.write(traceback.format_exc())
    finally:
        # Restore state
        try:
            os.chdir(old_cwd)
        except Exception:
            pass

        if old_syspath0 is None:
            # sys.path was empty before
            if sys.path:
                sys.path.pop(0)
        else:
            sys.path[0] = old_syspath0

    return rc, out.getvalue(), err.getvalue()



def run_all_parallel(path_dir, script_names, max_workers=None, chunksize=1):
    """
    Created by ChatGPT5.2 and effectively untested 
    Parallel execution with minimal overhead:
    - persistent worker processes (no per-script interpreter startup)
    - per-process stdout/stderr capture (no thread collisions)

    Returns dict[name] = {"returncode": int, "stdout": str, "stderr": str}
    """
    paths = [os.path.join(path_dir, n) for n in script_names]

    # "spawn" is safest/most portable (macOS/Windows). On Linux, "fork" can be faster,
    # but spawn avoids weird inherited-state bugs.
    ctx = mp.get_context("spawn")

    if max_workers is None:
        max_workers = min(len(paths), os.cpu_count() or 1)
    logging.debug(f"max_workers=({max_workers})")

    results = {}
    with ProcessPoolExecutor(max_workers=max_workers, mp_context=ctx) as ex:
        # map() has lower overhead than submit/as_completed, and chunksize reduces IPC overhead.
        for name, (rc, stdout, stderr) in zip(
            script_names,
            ex.map(_exec_script, paths, chunksize=chunksize),
        ):
            results[name] = {"returncode": rc, "stdout": stdout, "stderr": stderr}

    return results


def print_errors(results):

    def final_line(s):
        return next((line.lstrip() for line in reversed(s.splitlines()) if line.strip()), "")

    print()
    print("errors:")
    for loop_script in results.keys():
        if results[loop_script]['returncode'] == 0:
            continue
        loop_msg = final_line(results[loop_script]['stderr'])
        print("%s:\n\t%s" % (loop_script, loop_msg))


def print_summary(results, start_time, end_time):
    num_total = len(results)

    scripts_failed = [ script for script in results.keys() if results[script]['returncode'] != 0 ]
    scripts_succeesses = [ script for script in results.keys() if results[script]['returncode'] == 0 ]

    num_failures = len(scripts_failed)
    num_successes = len(scripts_succeesses)
    assert num_failures + num_successes == len(results.keys()), "Length of failures plus successes should equal scripts run"


    elapsed_seconds = (end_time - start_time) / 1000000000

    print()
    print(f"time to run solutions: {elapsed_seconds} seconds")
    print(f"total: {num_total}")
    print(f"successes: {num_successes}")
    print(f"failures: {num_failures}")


#   {{{
#def run_all_parallel_1(path_dir, script_names, max_workers=None, timeout=None):
#    """
#    Created by ChatGPT5.2
#    Runs each Python script in a separate interpreter process in parallel.
#    Returns a dict: {script_name: {"returncode": int, "stdout": str, "stderr": str}}
#    Not actually any faster than single threaded version
#    """
#    def _run_one(name):
#        #logging.debug(f"run=({name})")
#        path_script = os.path.join(path_dir, name)
#        # -u for unbuffered stdout/stderr (better for capture in real time-ish)
#        cp = subprocess.run(
#            [sys.executable, "-u", path_script],
#            cwd=path_dir,
#            capture_output=True,
#            text=True,
#            timeout=timeout,
#        )
#        #logging.debug(f"stdout=({cp.stdout})")
#        #logging.debug(f"stderr=({cp.stderr})")
#        #logging.debug(f"rc=({cp.returncode})")
#        return name, {"returncode": cp.returncode, "stdout": cp.stdout, "stderr": cp.stderr}
#    results = {}
#    # ThreadPool is fine here because each task is "wait for a subprocess"
#    with ThreadPoolExecutor(max_workers=max_workers) as ex:
#        futures = [ex.submit(_run_one, name) for name in script_names]
#        for fut in as_completed(futures):
#            name, res = fut.result()  # re-raises exceptions (e.g., timeout)
#            results[name] = res
#    return results
#
#def run_all_parallel_2(path_dir, script_names, max_workers=None, timeout=None):
#    """
#    Created by ChatGPT5.2
#    Run scripts in parallel, but cap concurrency to avoid oversubscribing CPU.
#    Returns:
#        dict[name] = {"returncode": int, "stdout": str, "stderr": str}
#    Still slower than single threaded version
#    """
#    cpu = os.cpu_count() or 1
#    if max_workers is None:
#        # For CPU-bound scripts, starting with <= cores is usually best.
#        max_workers = min(len(script_names), cpu)
#    def _run_one(name):
#        path_script = os.path.join(path_dir, name)
#        cp = subprocess.run(
#            [sys.executable, "-u", path_script],
#            cwd=path_dir,
#            capture_output=True,
#            text=True,
#            timeout=timeout,
#        )
#        return name, {"returncode": cp.returncode, "stdout": cp.stdout, "stderr": cp.stderr}
#    results = {}
#    with ThreadPoolExecutor(max_workers=max_workers) as ex:
#        futures = [ex.submit(_run_one, name) for name in script_names]
#        for fut in as_completed(futures):
#            name, res = fut.result()
#            results[name] = res
#    return results
#   }}}
#   {{{
#def run_all_single(path_dir, script_names):
#    for name in script_names:
#        path_script = os.path.join(path_dir, name)
#        runner(path_script)
#   }}}
#   {{{
#from concurrent.futures import ThreadPoolExecutor, as_completed
#def run_all_parallel_1(path_dir, script_names):
#    """Created by ChatGPT5.2
#    fails with 'ValueError('I/O operation on closed file')'"""
#    import os
#    from concurrent.futures import ThreadPoolExecutor
#    def _run_one(path_dir: str, name: str):
#        path_script = os.path.join(path_dir, name)
#        print(path_script)
#        return runner(path_script)
#    max_workers = 10
#    with ThreadPoolExecutor(max_workers=max_workers) as ex:
#        # Forces completion and re-raises exceptions from worker threads
#        list(ex.map(lambda n: _run_one(path_dir, n), script_names))
#
#def run_all_parallel_2(path_dir, script_names):
#    import os
#    from concurrent.futures import ProcessPoolExecutor
#    def _run_one(args):
#        path_dir, name = args
#        path_script = os.path.join(path_dir, name)
#        return runner(path_script)
#    max_workers = 10
#    with ProcessPoolExecutor(max_workers=max_workers) as ex:
#        list(ex.map(_run_one, [(path_dir, n) for n in script_names]))
#
#def run_all_parallel_3(path_dir, script_names):
#    import os
#    from concurrent.futures import ThreadPoolExecutor, as_completed
#    max_workers = 10
#    with ThreadPoolExecutor(max_workers=max_workers) as ex:
#        futures = {}
#        for name in script_names:
#            path_script = os.path.join(path_dir, name)
#            futures[ex.submit(runner, path_script)] = name
#
#        for fut in as_completed(futures):
#            name = futures[fut]
#            try:
#                fut.result()  # raises if runner failed
#            except Exception as e:
#                # handle however you want:
#                raise RuntimeError(f"{name} failed") from e
#   }}}
#   {{{
#def runner(path_script):
#    print(f"run: {path_script}")
#    stdout, stderr, rc = execute_script(path_script)
#    logging.debug(f"stdout=({stdout})")
#    logging.debug(f"stderr=({stderr})")
#    logging.debug(f"rc=({rc})")
#def execute_script(script_path):
#    #   {{{
#    """
#    Executes a Python script located at the given path, capturing its output, errors, and return code.
#
#    Created by gpt-1o (AND ONLY SUPERFICIALLY TESTED)
#
#    The function changes the current working directory to the directory containing the script and temporarily
#    adds that directory to `sys.path` before execution. This ensures that any imports within the script of
#    modules or packages located in its own directory (or subdirectories) will work correctly. After execution,
#    it restores the original working directory and `sys.path`, even if exceptions occur.
#
#    Parameters:
#        script_path (str): The file path to the Python script to be executed.
#
#    Returns:
#        tuple:
#            - script_output (str): Captured standard output (`stdout`) from the script execution.
#            - script_errors (str): Captured standard error (`stderr`) from the script execution, including any exception tracebacks.
#            - return_code (int): The return code (`rc`) of the script execution.
#                - `0` if the script executed successfully without errors or called `sys.exit(0)`.
#                - The integer value provided to `sys.exit(N)` if called with an integer `N`.
#                - `1` if the script raised an unhandled exception or called `sys.exit()` with a non-integer argument.
#
#    Notes:
#        - **Working Directory**: The current working directory is temporarily changed to the script's directory during execution.
#        - **Module Search Path**: The script's directory is temporarily added to `sys.path` to allow module imports.
#        - **Isolation**: The script is executed in its own isolated global namespace to prevent interference with the main program or other scripts.
#        - **Output Capturing**: Standard output and standard error are redirected to capture the script's outputs.
#        - **Exception Handling**:
#            - Unhandled exceptions are caught, and their tracebacks are captured in `script_errors`.
#            - `SystemExit` exceptions from `sys.exit()` calls are handled to determine the appropriate return code.
#        - **Return Code Simulation**: The function simulates the return code behavior of executing a script from the terminal.
#
#    Example:
#        ```python
#        output, errors, rc = execute_script('path/to/your/script.py')
#        print("Script Output:")
#        print(output)
#        if errors:
#            print("Script Errors:")
#            print(errors)
#        print(f"Return Code: {rc}")
#        ``` 
#    """
#    import os
#    import io
#    import sys
#    import traceback
#    import contextlib
#
#    # Create StringIO objects to capture stdout and stderr
#    stdout_capture = io.StringIO()
#    stderr_capture = io.StringIO()
#
#    # Read the script content
#    with open(script_path, 'r') as file:
#        script_code = file.read()
#
#    # Prepare an isolated global namespace for the script
#    script_globals = {
#        '__file__': script_path,
#        '__name__': '__main__',
#        '__package__': None,
#        '__builtins__': __builtins__,
#    }
#
#    # Initialize return code
#    return_code = 0
#
#    # Get the directory of the script
#    script_dir = os.path.dirname(os.path.abspath(script_path))
#    # Save the current working directory
#    original_cwd = os.getcwd()
#    # Save the original sys.path
#    original_sys_path = sys.path.copy()
#
#    # Redirect stdout and stderr to capture outputs
#    with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stderr_capture):
#        try:
#            # Change the current working directory to the script's directory
#            os.chdir(script_dir)
#            # Temporarily insert the script's directory at the beginning of sys.path
#            sys.path.insert(0, script_dir)
#            try:
#                # Execute the script code in the isolated namespace
#                exec(script_code, script_globals)
#            except SystemExit as e:
#                # Capture sys.exit() calls
#                if e.code is None:
#                    return_code = 0
#                elif isinstance(e.code, int):
#                    return_code = e.code
#                else:
#                    # sys.exit("error message") sets code to 1
#                    return_code = 1
#                    print(e.code, file=stderr_capture)
#            except Exception:
#                # Unhandled exceptions result in return code 1
#                return_code = 1
#                # Capture the exception traceback
#                traceback.print_exc(file=stderr_capture)
#        finally:
#            # Restore the original working directory
#            os.chdir(original_cwd)
#            # Restore the original sys.path
#            sys.path = original_sys_path
#
#    # Retrieve the captured outputs
#    script_output = stdout_capture.getvalue()
#    script_errors = stderr_capture.getvalue()
#
#    # Close the StringIO objects
#    stdout_capture.close()
#    stderr_capture.close()
#
#    return script_output, script_errors, return_code
#    #   }}}
#   }}}
#   {{{
#   {{{
#def execute_script(script_path):
#    #   {{{
#    """
#    Executes a Python script located at the given path, capturing its output, errors, and return code.
#
#    The function changes the current working directory to the directory containing the script before execution,
#    simulating the environment as if the script were run directly from its own directory. It captures the script's
#    standard output and standard error streams by redirecting them to `StringIO` objects. The function handles the
#    script's exit status by interpreting `sys.exit()` calls and unhandled exceptions, mimicking the behavior of running
#    the script directly from the terminal.
#
#    Parameters:
#        script_path (str): The file path to the Python script to be executed.
#
#    Returns:
#        tuple:
#            - script_output (str): Captured standard output (`stdout`) from the script execution.
#            - script_errors (str): Captured standard error (`stderr`) from the script execution, including any exception tracebacks.
#            - return_code (int): The return code (`rc`) of the script execution.
#                - `0` if the script executed successfully without errors or called `sys.exit(0)`.
#                - The integer value provided to `sys.exit(N)` if called with an integer `N`.
#                - `1` if the script raised an unhandled exception or called `sys.exit()` with a non-integer argument.
#
#    Notes:
#        - **Working Directory**: The current working directory is temporarily changed to the script's directory during execution.
#          After execution, it is restored to the original working directory, even if exceptions occur.
#        - **Isolation**: The script is executed in its own isolated global namespace to prevent interference with the main program or other scripts.
#        - **Output Capturing**: Standard output and standard error are redirected to capture the script's outputs.
#        - **Exception Handling**:
#            - Unhandled exceptions are caught, and their tracebacks are captured in `script_errors`.
#            - `SystemExit` exceptions from `sys.exit()` calls are handled to determine the appropriate return code.
#        - **Return Code Simulation**: The function simulates the return code behavior of executing a script from the terminal.
#
#    Example:
#        ```python
#        output, errors, rc = execute_script('path/to/your/script.py')
#        print("Script Output:")
#        print(output)
#        if errors:
#            print("Script Errors:")
#            print(errors)
#        print(f"Return Code: {rc}")
#        ```
#    """
#    import os
#    import io
#    import sys
#    import traceback
#    import contextlib
#
#    # Create StringIO objects to capture stdout and stderr
#    stdout_capture = io.StringIO()
#    stderr_capture = io.StringIO()
#
#    # Read the script content
#    with open(script_path, 'r') as file:
#        script_code = file.read()
#
#    # Prepare an isolated global namespace for the script
#    script_globals = {
#        '__file__': script_path,
#        '__name__': '__main__',
#        '__package__': None,
#        '__builtins__': __builtins__,
#    }
#
#    # Initialize return code
#    return_code = 0
#
#    # Get the directory of the script
#    script_dir = os.path.dirname(os.path.abspath(script_path))
#    # Save the current working directory
#    original_cwd = os.getcwd()
#
#    # Redirect stdout and stderr to capture outputs
#    with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stderr_capture):
#        try:
#            # Change the current working directory to the script's directory
#            os.chdir(script_dir)
#            try:
#                # Execute the script code in the isolated namespace
#                exec(script_code, script_globals)
#            except SystemExit as e:
#                # Capture sys.exit() calls
#                if e.code is None:
#                    return_code = 0
#                elif isinstance(e.code, int):
#                    return_code = e.code
#                else:
#                    # sys.exit("error message") sets code to 1
#                    return_code = 1
#                    print(e.code, file=stderr_capture)
#            except Exception:
#                # Unhandled exceptions result in return code 1
#                return_code = 1
#                # Capture the exception traceback
#                traceback.print_exc(file=stderr_capture)
#        finally:
#            # Change back to the original working directory
#            os.chdir(original_cwd)
#
#    # Retrieve the captured outputs
#    script_output = stdout_capture.getvalue()
#    script_errors = stderr_capture.getvalue()
#
#    # Close the StringIO objects
#    stdout_capture.close()
#    stderr_capture.close()
#
#    return script_output, script_errors, return_code
#    #   }}}
#   }}}
#   {{{
#def execute_script(script_path):
#    #   {{{
#    """
#    Executes a Python script located at the given path, capturing its output, errors, and return code.
#
#    This function reads the content of the specified Python script and executes it within an isolated global namespace.
#    It captures the script's standard output and standard error streams by redirecting them to `StringIO` objects.
#    The function handles the script's exit status by interpreting `sys.exit()` calls and unhandled exceptions,
#    mimicking the behavior of running the script directly from the terminal.
#
#    Parameters:
#        script_path (str): The file path to the Python script to be executed.
#
#    Returns:
#        tuple:
#            - script_output (str): Captured standard output (`stdout`) from the script execution.
#            - script_errors (str): Captured standard error (`stderr`) from the script execution, including any exception tracebacks.
#            - return_code (int): The return code (`rc`) of the script execution.
#                - `0` if the script executed successfully without errors or called `sys.exit(0)`.
#                - The integer value provided to `sys.exit(N)` if called with an integer `N`.
#                - `1` if the script raised an unhandled exception or called `sys.exit()` with a non-integer argument.
#
#    Notes:
#        - **Isolation**: The script is executed in its own isolated global namespace to prevent interference with the main program or other scripts.
#        - **Output Capturing**: Standard output and standard error are redirected to capture the script's outputs.
#        - **Exception Handling**:
#            - Unhandled exceptions are caught, and their tracebacks are captured in `script_errors`.
#            - `SystemExit` exceptions from `sys.exit()` calls are handled to determine the appropriate return code.
#        - **Return Code Simulation**: The function simulates the return code behavior of executing a script from the terminal.
#
#    Example:
#        ```python
#        output, errors, rc = execute_script('path/to/your/script.py')
#        print("Script Output:")
#        print(output)
#        if errors:
#            print("Script Errors:")
#            print(errors)
#        print(f"Return Code: {rc}")
#        ```
#
#        Created by gpt-o1
#    """
#
#    # Create StringIO objects to capture stdout and stderr
#    stdout_capture = io.StringIO()
#    stderr_capture = io.StringIO()
#
#    # Read the script content
#    with open(script_path, 'r') as file:
#        script_code = file.read()
#
#    # Prepare an isolated global namespace for the script
#    script_globals = {
#        '__file__': script_path,
#        '__name__': '__main__',
#        '__package__': None,
#        '__builtins__': __builtins__,
#    }
#
#    # Initialize return code
#    return_code = 0
#
#    # Redirect stdout and stderr to capture outputs
#    with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stderr_capture):
#        try:
#            # Execute the script code in the isolated namespace
#            exec(script_code, script_globals)
#        except SystemExit as e:
#            # Capture sys.exit() calls
#            if e.code is None:
#                return_code = 0
#            elif isinstance(e.code, int):
#                return_code = e.code
#            else:
#                # sys.exit("error message") sets code to 1
#                return_code = 1
#                print(e.code, file=stderr_capture)
#        except Exception:
#            # Unhandled exceptions result in return code 1
#            return_code = 1
#            # Capture the exception traceback
#            traceback.print_exc(file=stderr_capture)
#
#    # Retrieve the captured outputs
#    script_output = stdout_capture.getvalue()
#    script_errors = stderr_capture.getvalue()
#
#    # Close the StringIO objects
#    stdout_capture.close()
#    stderr_capture.close()
#
#    return script_output, script_errors, return_code
#    #   }}}
#   }}}
#   {{{
#def execute_script(script_path):
#    import traceback
#    import contextlib
#    import io
#
#    # Create StringIO objects to capture stdout and stderr
#    stdout_capture = io.StringIO()
#    stderr_capture = io.StringIO()
#
#    # Read the script content
#    with open(script_path, 'r') as file:
#        script_code = file.read()
#
#    # Prepare an isolated global namespace for the script
#    script_globals = {
#        '__file__': script_path,
#        '__name__': '__main__',
#        '__package__': None,
#        '__builtins__': __builtins__,
#    }
#
#    # Redirect stdout and stderr to capture outputs
#    with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stderr_capture):
#        try:
#            # Execute the script code in the isolated namespace
#            exec(script_code, script_globals)
#        except Exception:
#            # Capture the exception traceback
#            traceback.print_exc(file=stderr_capture)
#
#    # Retrieve the captured outputs
#    script_output = stdout_capture.getvalue()
#    script_errors = stderr_capture.getvalue()
#
#    # Close the StringIO objects
#    stdout_capture.close()
#    stderr_capture.close()
#
#    return script_output, script_errors
#
#def runner_execute_script_in_same_process(script_path):
#    """
#    Doesn't handle exceptions
#    """
#    with open(script_path, 'r') as file:
#        script_code = file.read()
#    # Execute the script code within the same global namespace
#    exec(script_code, globals())
#
#def runner_import_and_execute(script_path):
#    """
#    Doesn't handle exceptions
#    ... also it's not doing anything with 'module.main()', instead the execution happens during (what?) stage?
#    """
#    import importlib.util
#    module_name = 'imported_script'
#    spec = importlib.util.spec_from_file_location(module_name, script_path)
#    module = importlib.util.module_from_spec(spec)
#    sys.modules[module_name] = module
#    spec.loader.exec_module(module)
#    # If the script defines a main() function, call it
#    if hasattr(module, 'main'):
#        module.main()
#
#def runner_subprocess(path_script):
#    """INCORRECT?!"""
#    import subprocess
#    logging.debug(f"path_script=({path_script})")
#    if not os.path.isfile(path_script):
#        raise FileNotFoundError(path_script)
#    try:
#        # Run the script using the Python interpreter
#        result = subprocess.run(
#            ['python', path_script],
#            capture_output=True,
#            text=True,
#            check=True
#        )
#        # Print the script's output
#        print('Output:', result.stdout)
#    except subprocess.CalledProcessError as e:
#        print('An error occurred while executing the script:')
#        print('Return code:', e.returncode)
#        print('Error output:', e.stderr)
#   }}}
#   }}}


def main():
    parent_dir = get_self_parent_dir()
    script_names = get_scriptnames(parent_dir)
    max_workers = None
    chunksize = 1
    #script_names = [ '884-uncommon-words-in-two-sentences.py', '1544-make-string-great.py', ]
    start_time = time.time_ns()
    results = run_all_parallel(parent_dir, script_names, max_workers, chunksize)
    end_time = time.time_ns()
    print_errors(results)
    print_summary(results, start_time, end_time)


if __name__ == '__main__':
    main()
    logging.debug("DONE")

