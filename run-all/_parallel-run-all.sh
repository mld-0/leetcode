#!/usr/bin/env sh
#	{{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#	{{{2
#	Ongoings:
#	{{{
#	Ongoing: 2024-05-27T20:53:48AEST do we really need a tempdir for each script (surely we can just create files for each)
#	Ongoing: 2024-05-27T20:54:20AEST calling `mkdir` so many times is sloooow (batch create tmpdirs)
#	Ongoing: 2024-05-27T20:54:51AEST each function in this script would be better (faster) implemented in python?
#	Ongoing: 2024-05-27T21:53:42AEST update `call_get_scripts_list()` to also get python 'resources' classes (eg: linkedlist, treenode) so they can be run as well (or get them seperately, and update functions to take list of scripts as argument instead of using global variable)
#	Ongoing: 2024-05-27T21:55:49AEST running non-python solutions: here or elsewhere? (if elsewhere, we want a single script which runs everything we've written in leetcode directory)
#	Ongoing: 2024-05-27T21:56:38AEST this script does everything `_run-all.sh` does better. For a single-threaded version, simple remove the `( ) & wait` from the main loop of `run_scripts_list_parallel()`
#	}}}

#set -o errexit   	# abort on nonzero exitstatus
set -o nounset   	# abort on unbound variable
set -o pipefail  	# don't hide errors within pipes
nl=$'\n'


#	Must be run from within containing directory
#	(we need to find `path_script_get_numbered`)


bin_py="python3.11"
path_script_get_numbered="get-numbered-problems.sh"
flag_report_failed_scripts=1
flag_report_failed_scripts_errors=1
flag_printOutput=0
flag_cleanupOnFinish=0
path_tmp=`mktemp -d`

call_get_scripts_list() 
{
	local path_script="$1"
	if [[ ! -f "$path_script" ]]; then
		echo "error, not found, path_script=($path_script)" > /dev/stderr
		exit 2
	fi
	IFS_temp="$IFS"
	IFS=$'\n'
	scripts_list=( $( $SHELL "$path_script_get_numbered" ) )
	IFS="$IFS_temp"
	if [[ ${#scripts_list[@]} -le 0 ]]; then 
		echo "error, scripts_list=(${scripts_list[@]})" > /dev/stderr; 
		exit 2; 
	fi
	echo "found: ${#scripts_list[@]} python solutions"
}

setup_tmpdirs() 
{
	echo "path_tmp=($path_tmp)"
	for loop_script in "${scripts_list[@]}"; do
		loop_script_filename=$( basename "$loop_script" )
		current_tmp="$path_tmp/$loop_script_filename"
		mkdir -p "$current_tmp"
	done
}

run_scripts_list_parallel() 
{
	echo "bin_py=($bin_py)"
	touch "$path_tmp/failured-scripts-log"
	local time_start=$( perl -MTime::HiRes=time -E 'printf "%.6f\n", time' )
	echo "$time_start" > "$path_tmp/time-start"
	for loop_script in "${scripts_list[@]}"; do
	(
		loop_script_filename=$( basename "$loop_script" )
		current_tmp="$path_tmp/$loop_script_filename"
		run_msg="./$loop_script_filename"
		#$bin_py $loop_script_filename > "$current_tmp/my-stdout" 2> "$current_tmp/my-stderr"
		echo "$run_msg"
		#echo "$loop_script_filename:"
		$bin_py $loop_script > "$current_tmp/my-stdout" 2> "$current_tmp/my-stderr"
		echo "$?" > "$current_tmp/my-rc" ; 
		rc=`cat "$current_tmp/my-rc"`
		if [[ $rc -ne 0 ]]; then
			echo "$loop_script_filename" > "$current_tmp/failed"
			echo "$loop_script_filename" >> "$path_tmp/failured-scripts-log"
		fi
		if [[ $flag_printOutput -ne 0 ]]; then
			cat "$current_tmp/my-stdout" | grep -v "^$"
			echo "rc=($rc)"
			echo ""
		fi
	) &
	done
	wait
	local time_end=$( perl -MTime::HiRes=time -E 'printf "%.6f\n", time' )
	echo "$time_end" > "$path_tmp/time-end"
}

report_errors() 
{
	if [[ $flag_report_failed_scripts -eq 0 ]]; then return; fi
	cd "$path_tmp"
	echo ""
	echo "errors:"
	for dir in $( find . -maxdepth 1 -type d | cut -c 3- | sort -h ); do
		failure_file="$dir/failed"
		stderr_file="$dir/my-stderr"
		loop_scriptname=`basename $dir`
		if [ -f "$failure_file" ]; then
			msg_stderr=`cat "$stderr_file" | tail -n 1 | sed "s/^/\t/g"`
			if [[ $flag_report_failed_scripts_errors -ne 0 ]]; then
				echo "$loop_scriptname:$nl$msg_stderr"
			else
				echo "$loop_scriptname"
			fi
		fi
	done
}

report_summary() 
{
	local num_total="${#scripts_list[@]}"
	local num_failures=$( cat "$path_tmp/failured-scripts-log" | wc -l )
	local num_succeses=$( perl -E "say $num_total - $num_failures" )
	local time_start=`cat "$path_tmp/time-start"`
	local time_end=`cat "$path_tmp/time-end"`
	local time_elapsed=$( perl -E "printf \"%.6f\n\", $time_end - $time_start" )
	echo ""
	echo "time to run solutions: $time_elapsed seconds"
	echo "total: $num_total"
	echo "successes: $num_succeses"
	echo "failures: $num_failures"
}

validate_command() 
{
	local bin_cmd="$1"
	if ! command -v $bin_cmd &> /dev/null; then
	    echo "error, command=($bin_cmd) could not be found" > /dev/stderr
	    exit 2
	fi
}

cleanup_tmpdir() 
{
	local flag_cleaup="$1"
	local path_dir="$2"
	if [[ $flag_cleaup -ne 0 ]]; then
		rm -r "$path_tmp"
	fi
}

main() 
{
	validate_command "$bin_py"
	call_get_scripts_list "$path_script_get_numbered"
	setup_tmpdirs
	run_scripts_list_parallel
	report_errors
	report_summary
	cleanup_tmpdir "$flag_cleanupOnFinish" "$path_tmp" 
}

main

