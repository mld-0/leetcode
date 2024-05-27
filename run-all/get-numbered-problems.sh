#!/usr/bin/env sh
#	{{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#	{{{2
set -o errexit   # abort on nonzero exitstatus
set -o nounset   # abort on unbound variable
set -o pipefail  # don't hide errors within pipes

path_self="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
if [[ ! -d "$path_self" ]]; then
	echo "error, not found, path_self=($path_self)" > /dev/stderr
	exit 2
fi

cd "$path_self/.."
find . -regex "^\./[0-9].*\.py$" | sort -V | sed "s|^\./|$PWD/|g"

