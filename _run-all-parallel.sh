#!/usr/bin/env sh

#set -o errexit   # abort on nonzero exitstatus
set -o nounset   # abort on unbound variable
set -o pipefail  # don't hide errors within pipes

scripts_list=( $( find . -regex "^\./[0-9].*\.py$" | sort ) )
time_start=$( perl -MTime::HiRes=time -E 'printf "%.6f\n", time' )

for loop_script in "${scripts_list[@]}"; do
	(
	echo "$loop_script:"
	time ( python3 $loop_script | perl -nE 'print if not /^$/' )
	echo ""
	) &
done
wait

time_end=$( perl -MTime::HiRes=time -E 'printf "%.6f\n", time' )
time_elapsed=$( perl -E "say $time_end - $time_start" )
echo "time_elapsed=($time_elapsed)"

