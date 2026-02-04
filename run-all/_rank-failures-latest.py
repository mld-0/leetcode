import sys
import os
import re
import subprocess
import logging
import itertools
import concurrent
import concurrent.futures
from datetime import datetime

#logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logging.basicConfig(stream=sys.stderr, level=logging.WARNING)

version = "2026.02.04"

#   Usage:
#   #>$     python3 _parallel-run-all.py 2> /dev/null | python3 _rank-failures-latest.py
#   (Taking list of failed scripts with exceptions and querying creation, modification, and commit times)
#   Requires report of failures to be in the following format:
#   (This is included in output currently (version 2026-02-04) by both python/shell parallel-run-all scripts)
#       - Begins with line "errors:"
#       - Finishes with empty line
#       - Alternating lines with filename and last line from stderr when run (name of the exception)
#   
#   Uses untested StackOverflow function `creation_date()` to (attempt to) get 


def parse_runall_output_get_failures(input_lines):
    """Given the input as a list of lines, extract the filename, return code, and error message, as printed by the `_parallel-run-all.sh` script.
    These lines are in the format: 'rc=(1): ./05-longest-palindromic-substring.py: NotImplementedError: Complete `TwoPointers_ClarifyIndexes`'"""


    def resolve_filename(filename):
        if os.path.isfile(filename):
            return filename
        else:
            old_filename = filename
            filename = os.path.join("../", filename)
            if not os.path.isfile(filename):
                raise Exception(f"Could not find filename=({old_filename}) in current or parent directory")
            return filename

    #   If given a list of strings, turn it into a single string
    if type(input_lines) == type([]):
        input_lines = ''.join(input_lines)
    logging.debug(f"input_lines=({input_lines})")

    re_failure_report = re.compile(
            r"(?ms)^[ \t]*errors:[ \t]*\r?\n"   # the header line
            r"(.*?)"                            # capture lazily
            r"(?=^\s*\r?\n)",                   # stop before first blank line
    )
    logging.debug(f"re_failure_report=({re_failure_report})")

    temp = re_failure_report.search(input_lines)
    failure_report_paragraph = temp.group(1) if temp else ""
    #logging.debug(f"failure_report_paragraph=({failure_report_paragraph})")


    failure_report_paragraph = failure_report_paragraph.splitlines()
    assert len(failure_report_paragraph) % 2 == 0 \
        , "sanity check: length of failure_report_paragraph should be even"


    failures = []
    for line_file, line_exception in zip(failure_report_paragraph[0::2], failure_report_paragraph[1::2]):
        #logging.debug(f"line_file=({line_file}), line_exception=({line_exception})")
        match_file = line_file.rstrip(":")
        match_exception = line_exception.strip()
        #logging.debug(f"match_file=({match_file}), match_exception=({match_exception})")
        match_file = resolve_filename(match_file)
        match_record = { 'filename': match_file, 'message': match_exception, 'rc': None, }
        failures.append(match_record)

    if len(failures) == 0:
        raise Exception("No Failed Scripts Found")
    logging.debug(f"len(failures)=({len(failures)})")

    return failures




def add_last_modified(files):
    """For each dictionary in a list, add (in-place) record['mtime'] = mtime and record['ctime'] = ctime
        Each dictionary must contain the filename under the key 'filename' (which must exist)"""

    def creation_date(path_to_file):
        """
        CURRENTLY UNTESTED
        REQUIRES 'statx' on Linux
        Try to get the Unix timestamp that a file was created, falling back to when
        it was last modified if that isn't possible.
        See http://stackoverflow.com/a/39501288/1709587 for explanation.
        From: https://stackoverflow.com/questions/237079/how-do-i-get-file-creation-and-modification-date-times
        """
        import os
        import platform
        if platform.system() == 'Windows':
            return os.path.getctime(path_to_file)
        else:
            stat = os.stat(path_to_file)
            try:
                return stat.st_birthtime
            except AttributeError:
                # We're probably on Linux. Hopefully, we are on a recent enough
                # version that we can use the statx syscall. (If we are not, btime
                # below will be `None`.)
                try:
                    from statx import statx
                except ImportError:
                    logging.warning("Couldn't import `statx`, failed to get creation date (return None)")
                    return None
                btime = statx(path_to_file).btime
                if btime:
                    return btime
        # If we've made it this far, all our efforts have failed. Fall back to
        # returning last-modified time as the closest available alternative:
        #logging.warning("failed to get creation date, default to modification date")
        #return os.path.getmtime(path_to_file)
        logging.warning("failed to get creation date (return None)")
        return None

    for record in files:
        filename = record['filename']
        if not os.path.isfile(filename):
            raise FileNotFoundError(filename)
        mtime = os.path.getmtime(filename)
        ctime = os.path.getctime(filename)
        creation_time = creation_date(filename)
        record['mtime'] = mtime
        record['ctime'] = ctime
        record['creation'] = creation_time


def add_git_history(files):
    """For each dictionary in a list, add (in-place) the git history and last commit time
        Each dictionary must contain the filename under the key 'filename' (which must exist)
        If the file has been committed, record['git_history'] = (epochs, hashes) (where `epochs` and `hashes` are a list of the epoch and has of each commit, and record['last_commit_time'] = the epoch of the most recent commit. If the file has not been committed, both are set to None."""
    def process_record(record):
        filename = record['filename']
        if not os.path.isfile(filename):
            raise FileNotFoundError(filename)
        git_history = get_git_history(filename)
        record['git_history'] = git_history
        last_commit_time = 0
        if git_history is not None and len(git_history) > 0:
            last_commit_time = git_history[0][0]  # Assuming git_history is a list of tuples (hash, epoch_time)
        record['last_commit_time'] = last_commit_time
        return record
    def run_parallel(files):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(process_record, record) for record in files]
            for future in concurrent.futures.as_completed(futures):
                updated_record = future.result()
    run_parallel(files)


def get_git_history(filename):
    """For a given file, if it has been committed, return a list of the epoch of each commit and a list of the hash of each commit (otherwise None)"""
    try:
        result = subprocess.run(['git', 'log', '--pretty=format:%H %at', filename], check=True, text=True, capture_output=True)
        if result.stdout:
            hashes = []
            epochs = []
            for line in result.stdout.strip().split('\n'):
                commit_hash, epoch_time = line.split(' ')
                hashes.append(commit_hash)
                epochs.append(float(epoch_time))
            return ( epochs, hashes, )
        else:
            return None
    except subprocess.CalledProcessError as e:
        logging.warning(f"get_git_history failed for filename=({filename}), e=({e})")
        return None


def report_results(files):
    report_by_time(files, 'mtime')
    print()
    report_by_time(files, 'creation')
    print()
    report_by_time(files, 'last_commit_time')
    print()


def report_by_time(files, sortby):
    #logging.debug(f"files=({files})")
    items = [ (x['filename'], x[sortby], x) for x in files ]
    items.sort(key=lambda x: [ x[1], x[0] ], reverse=True)
    datetime_format = '%Y-%m-%d %H:%M:%S'
    print(f"sortby: {sortby}")
    for (filename, epoch, record) in items:
        datetime_str = datetime.fromtimestamp(epoch).strftime(datetime_format)
        print(f"{datetime_str}: {filename}")


def report_differences_in_order(files, sortby_1, sortby_2):
    """When sorting by two different times (eg, mtime and last_commit_time), summarise the differences in the resulting order"""
    raise NotImplementedError()


def main():
    input_lines = sys.stdin.readlines()
    failures = parse_runall_output_get_failures(input_lines)
    add_last_modified(failures)
    add_git_history(failures)
    report_results(failures)


if __name__ == '__main__':
    main()

