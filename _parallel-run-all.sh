#!/usr/bin/env sh
#	{{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#	{{{2

bin_py=python3.11
flag_printOutput=0

IFS_temp="$IFS"
IFS=$'\n'
scripts_list=( $( find . -regex "^\./[0-9].*\.py$" | sort -V ) )
IFS="$IFS_temp"

path_tmp=`mktemp -d`
path_failures="$path_tmp/failures-report"

#	validate: bin_py, path_tmp, scripts_list
#	{{{
if ! command -v $bin_py &> /dev/null; then
    echo "bin_py=($bin_py) could not be found" > /dev/stderr
    exit
fi
if [[ ! -d $path_tmp ]]; then
	echo "error, path_tmp=($path_tmp) not found" > /dev/stderr
	exit 2
fi
if [[ ${#scripts_list[@]} -le 0 ]]; then
	echo "error, scripts_list=(${scripts_list[@]})" > /dev/stderr
	exit 2
fi
#	}}}

#	Multi-file:
for loop_script in "${scripts_list[@]}"; do
	current_tmp="$path_tmp/$loop_script"
	mkdir "$current_tmp"
done
time_start=$( perl -MTime::HiRes=time -E 'printf "%.6f\n", time' )
i=0
for loop_script in "${scripts_list[@]}"; do
	(
	current_tmp="$path_tmp/$loop_script"
	path_failure=$current_tmp/my-failures
	path_stdout=$current_tmp/my-stdout
	path_stderr=$current_tmp/my-stderr
	path_rc=$current_tmp/my-rc
	echo "$loop_script:"
	$bin_py $loop_script > $path_stdout 2> $path_stderr 
	echo "$?" > $path_rc ; 
	rc=`cat $path_rc`
	if [[ $rc -ne 0 ]]; then
		echo "rc=($rc): $loop_script" >> $path_failure
		#cat $path_stderr
	fi
	if [[ $flag_printOutput -ne 0 ]]; then
		cat $path_stdout | grep -v "^$"
		echo "rc=($rc)"
		echo ""
	fi
	i=`perl -E "say $i+1"`
	) &
done
wait
time_end=$( perl -MTime::HiRes=time -E 'printf "%.6f\n", time' )
time_elapsed=$( perl -E "say $time_end - $time_start" )
cd "$path_tmp"
for dir in $( find . -maxdepth 1 -type d | cut -c 3- | sort -h ); do
    failure_file="$dir/my-failures"
	stderr_file="$dir/my-stderr"
    if [ -f "$failure_file" ]; then
		result=$( cat "$failure_file" )": "$( cat "$stderr_file" | tail -n 1 )
		echo "$result" >> "$path_failures"
    fi
done
num_total="${#scripts_list[@]}"
num_failures=$( cat "$path_failures" | wc -l )
num_succeses=$( perl -E "say $num_total - $num_failures" )

echo ""
echo "time_elapsed=($time_elapsed)"
echo "total: $num_total"
echo "successes: $num_succeses"
echo "failures: $num_failures"
cat $path_failures 

