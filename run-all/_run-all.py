#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import sys
import os
import io
import traceback
import contextlib
import re
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


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
    logging.debug(f"filenames=({filenames})")
    return filenames


def run_all(path_dir, script_names):
    for name in script_names:
        path_script = os.path.join(path_dir, name)
        runner(path_script)


def runner(path_script):
    print(f"run: {path_script}")
    stdout, stderr, rc = execute_script(path_script)
    logging.debug(f"stdout=({stdout})")
    logging.debug(f"stderr=({stderr})")
    logging.debug(f"rc=({rc})")


def execute_script(script_path):
    #   {{{
    """
    Executes a Python script located at the given path, capturing its output, errors, and return code.

    Created by gpt-1o (AND ONLY SUPERFICIALLY TESTED)

    The function changes the current working directory to the directory containing the script and temporarily
    adds that directory to `sys.path` before execution. This ensures that any imports within the script of
    modules or packages located in its own directory (or subdirectories) will work correctly. After execution,
    it restores the original working directory and `sys.path`, even if exceptions occur.

    Parameters:
        script_path (str): The file path to the Python script to be executed.

    Returns:
        tuple:
            - script_output (str): Captured standard output (`stdout`) from the script execution.
            - script_errors (str): Captured standard error (`stderr`) from the script execution, including any exception tracebacks.
            - return_code (int): The return code (`rc`) of the script execution.
                - `0` if the script executed successfully without errors or called `sys.exit(0)`.
                - The integer value provided to `sys.exit(N)` if called with an integer `N`.
                - `1` if the script raised an unhandled exception or called `sys.exit()` with a non-integer argument.

    Notes:
        - **Working Directory**: The current working directory is temporarily changed to the script's directory during execution.
        - **Module Search Path**: The script's directory is temporarily added to `sys.path` to allow module imports.
        - **Isolation**: The script is executed in its own isolated global namespace to prevent interference with the main program or other scripts.
        - **Output Capturing**: Standard output and standard error are redirected to capture the script's outputs.
        - **Exception Handling**:
            - Unhandled exceptions are caught, and their tracebacks are captured in `script_errors`.
            - `SystemExit` exceptions from `sys.exit()` calls are handled to determine the appropriate return code.
        - **Return Code Simulation**: The function simulates the return code behavior of executing a script from the terminal.

    Example:
        ```python
        output, errors, rc = execute_script('path/to/your/script.py')
        print("Script Output:")
        print(output)
        if errors:
            print("Script Errors:")
            print(errors)
        print(f"Return Code: {rc}")
        ``` 
    """
    import os
    import io
    import sys
    import traceback
    import contextlib

    # Create StringIO objects to capture stdout and stderr
    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()

    # Read the script content
    with open(script_path, 'r') as file:
        script_code = file.read()

    # Prepare an isolated global namespace for the script
    script_globals = {
        '__file__': script_path,
        '__name__': '__main__',
        '__package__': None,
        '__builtins__': __builtins__,
    }

    # Initialize return code
    return_code = 0

    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(script_path))
    # Save the current working directory
    original_cwd = os.getcwd()
    # Save the original sys.path
    original_sys_path = sys.path.copy()

    # Redirect stdout and stderr to capture outputs
    with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stderr_capture):
        try:
            # Change the current working directory to the script's directory
            os.chdir(script_dir)
            # Temporarily insert the script's directory at the beginning of sys.path
            sys.path.insert(0, script_dir)
            try:
                # Execute the script code in the isolated namespace
                exec(script_code, script_globals)
            except SystemExit as e:
                # Capture sys.exit() calls
                if e.code is None:
                    return_code = 0
                elif isinstance(e.code, int):
                    return_code = e.code
                else:
                    # sys.exit("error message") sets code to 1
                    return_code = 1
                    print(e.code, file=stderr_capture)
            except Exception:
                # Unhandled exceptions result in return code 1
                return_code = 1
                # Capture the exception traceback
                traceback.print_exc(file=stderr_capture)
        finally:
            # Restore the original working directory
            os.chdir(original_cwd)
            # Restore the original sys.path
            sys.path = original_sys_path

    # Retrieve the captured outputs
    script_output = stdout_capture.getvalue()
    script_errors = stderr_capture.getvalue()

    # Close the StringIO objects
    stdout_capture.close()
    stderr_capture.close()

    return script_output, script_errors, return_code
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
    #script_names = [ '884-uncommon-words-in-two-sentences.py', '1544-make-string-great.py', ]
    run_all(parent_dir, script_names)


if __name__ == '__main__':
    main()

