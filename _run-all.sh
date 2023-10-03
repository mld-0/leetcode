#!/usr/bin/env sh
#	{{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#	{{{2
#	Continue: 2023-03-22T22:37:29AEDT report number run / number failed

bin_py=python3.11
flag_printOutput=0

scripts_list=( $( find . -regex "^\./[0-9].*\.py$" | sort -V ) )

path_tmp=`mktemp -d`
path_failures=$path_tmp/my-failures
path_stdout=$path_tmp/my-stdout
path_stderr=$path_tmp/my-stderr
path_rc=$path_tmp/my-rc

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
#	delete: path_failures
#	{{{
if [[ -f $path_failures ]]; then
	rm $path_failures 
fi
#	}}}

time_start=$( perl -MTime::HiRes=time -E 'printf "%.6f\n", time' )

for loop_script in "${scripts_list[@]}"; do
	echo "$loop_script:"
	$bin_py $loop_script > $path_stdout 2> $path_stderr 
	echo "$?" > $path_rc ; 
	rc=`cat $path_rc`
	if [[ $rc -ne 0 ]]; then
		echo "rc=($rc): $loop_script" >> $path_failures
		cat $path_stderr
	fi
	if [[ $flag_printOutput -ne 0 ]]; then
		cat $path_stdout | grep -v "^$"
		echo "rc=($rc)"
		echo ""
	fi
done

time_end=$( perl -MTime::HiRes=time -E 'printf "%.6f\n", time' )
time_elapsed=$( perl -E "say $time_end - $time_start" )
echo ""
echo "time_elapsed=($time_elapsed)"
echo -n "failures: "; cat $path_failures | wc -l;
cat $path_failures

