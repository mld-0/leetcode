#!/usr/bin/env sh
#	{{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#	{{{2

#	Deprecated: 2024-05-27T21:51:31AEST `_parallel-run-all.sh` does everything this script does better. For a single-threaded version, simple remove the `( ) & wait` from the main loop of `run_scripts_list_parallel()` in said script

#set -o errexit   # abort on nonzero exitstatus
set -o nounset   # abort on unbound variable
set -o pipefail  # don't hide errors within pipes

bin_py=python3.11
path_script_get_numbered="get-numbered-problems.sh"
#	validate: path_script_get_numbered, bin_py
#	{{{
if [[ ! -f "$path_script_get_numbered" ]]; then
	echo "error, not found, path_self=($path_script_get_numbered)" > /dev/stderr
	exit 2 
fi
if ! command -v $bin_py &> /dev/null; then
    echo "bin_py=($bin_py) could not be found" > /dev/stderr
    exit 2
fi
#	}}}

flag_printOutput=0
flag_cleanupOnFinish=0
path_tmp=`mktemp -d`

#	run: path_script_get_numbered
IFS_temp="$IFS"; IFS=$'\n'; 
scripts_list=( $( $SHELL "$path_script_get_numbered" ) ); 
IFS="$IFS_temp";

#	validate: ${scripts_list[@]}
#	{{{
if [[ ${#scripts_list[@]} -le 0 ]]; then
	echo "error, scripts_list=(${scripts_list[@]})" > /dev/stderr
	exit 2
fi
#	}}}
#	declare: path_log_failures, path_log_stdout, path_log_stderr, path_log_rc,
#	{{{
path_log_failures=$path_tmp/my-failures
path_log_stdout=$path_tmp/my-stdout
path_log_stderr=$path_tmp/my-stderr
path_log_rc=$path_tmp/my-rc
#	}}}

#	run each script in: ${scripts_list[@]}
time_start=$( perl -MTime::HiRes=time -E 'printf "%.6f\n", time' )
for loop_script in "${scripts_list[@]}"; do
	loop_script_filename=$( basename "$loop_script" )
	echo "$loop_script_filename:"
	$bin_py $loop_script > $path_log_stdout 2> $path_log_stderr 
	echo "$?" > $path_log_rc ; 
	rc=`cat $path_log_rc`
	if [[ $rc -ne 0 ]]; then
		echo "rc=($rc): $loop_script_filename" >> $path_log_failures
		cat $path_log_stderr
	fi
	if [[ $flag_printOutput -ne 0 ]]; then
		cat $path_log_stdout | grep -v "^$"
		echo "rc=($rc)"
		echo ""
	fi
done
time_end=$( perl -MTime::HiRes=time -E 'printf "%.6f\n", time' )

time_elapsed=$( perl -E "say $time_end - $time_start" )
num_total="${#scripts_list[@]}"
num_failures=$( cat "$path_log_failures" | wc -l )
num_succeses=$( perl -E "say $num_total - $num_failures" )

echo ""
echo "time_elapsed=($time_elapsed)"
echo "total: $num_total"
echo "successes: $num_succeses"
echo "failures: $num_failures"
cat $path_log_failures

if [[ $flag_cleanupOnFinish -ne 0 ]]; then
	rm -r "$path_tmp"
fi

