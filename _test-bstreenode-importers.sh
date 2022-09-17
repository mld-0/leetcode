#!/usr/bin/env sh
#set -o errexit   # abort on nonzero exitstatus
set -o nounset   # abort on unbound variable
set -o pipefail  # don't hide errors within pipes
log_debug() { echo "$@" > /dev/stderr; }

bin_py=python3

#PWD_temp=$PWD
#SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
#cd "$SCRIPTPATH"

IFS_temp=$IFS
IFS=$'\n'
test_files=( $( grep -lIiw "TreeNode" *.py | sort -h ) )
IFS=$IFS_temp

for f in "${test_files[@]}"; do
	log_debug "f=($f)" 
	$bin_py "$f" 
	rc=$?
	log_debug "rc=($rc)"
	if [[ $rc -ne 0 ]]; then
		echo "Failed rc=($rc) for f=($f)"
		exit 2
	fi
done

log_debug "DONE"

#cd "$PWD_temp"

