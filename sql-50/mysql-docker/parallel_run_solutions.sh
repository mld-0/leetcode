#!/bin/bash

IFS_temp="$IFS"
IFS=$'\n'
scripts_list=( $( find . -regex "^\./[0-9]+-[0-9]+.*\.sh$" | sort -V ) )
IFS="$IFS_temp"

time_start=$( perl -MTime::HiRes=time -E 'printf "%.6f\n", time' )

for loop_script in "${scripts_list[@]}"; do
	(
	echo "$loop_script:"
	$SHELL "$loop_script"
	echo ""
	) &
done
wait

time_end=$( perl -MTime::HiRes=time -E 'printf "%.6f\n", time' )
time_elapsed=$( perl -E "say $time_end - $time_start" )
echo ""
echo "time_elapsed=($time_elapsed)"


