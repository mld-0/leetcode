#!/usr/bin/env python3
import sys
import os
import re
import subprocess
import logging
import concurrent
import concurrent.futures
from datetime import datetime
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
version = "2024.04.05"

#   Usage:
#   #>$ zsh _parallel-run-all.sh | python3 _rank-failures-latest.py

def parse_runall_output_get_failures(input_lines):
    """Given the input as a list of lines, extract the filename, return code, and error message, as printed by the `_parallel-run-all.sh` script.
    These lines are in the format: 'rc=(1): ./05-longest-palindromic-substring.py: NotImplementedError: Complete `TwoPointers_ClarifyIndexes`'"""
    failures = []
    re_failure = r'rc=\((\d+)\): \./(.*?): (.*$)'
    for line in input_lines:
        match = re.match(re_failure, line)
        if match:
            filename = match.group(2)
            rc_value = match.group(1)
            error = match.group(3)
            match_record = { 'filename': filename, 'rc': rc_value, 'message': error, }
            failures.append(match_record)
    return failures


def add_last_modified(files):
    """For each dictionary in a list, add (in-place) record['mtime'] = mtime and record['ctime'] = ctime
        Each dictionary must contain the filename under the key 'filename' (which must exist)"""
    for record in files:
        filename = record['filename']
        if not os.path.isfile(filename):
            raise FileNotFoundError(filename)
        mtime = os.path.getmtime(filename)
        ctime = os.path.getctime(filename)
        record['mtime'] = mtime
        record['ctime'] = ctime


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
    report_by_time(files, 'last_commit_time')
    print()


def report_by_time(files, sortby):
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

