set -o errexit   # abort on nonzero exitstatus
set -o nounset   # abort on unbound variable
set -o pipefail  # don't hide errors within pipes

$SHELL 'setup_mysql_container.sh'
$SHELL 'wait_until_mysql_container_running.sh'
$SHELL 'run_solutions.sh'
$SHELL 'cleanup_mysql_container.sh'

