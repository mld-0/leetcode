#!/bin/bash
source "$(dirname "$0")/config.sh"

echo "Waiting for MySQL to initialize:"
while ! docker exec $CONTAINER_NAME mysqladmin --user=root --password=$ROOT_PASSWORD --host "127.0.0.1" --port $MYSQL_PORT ping --silent 2>&1 | grep -v "Using a password on the command line interface can be insecure"; do
	sleep 1
	echo -n "."
done
echo "MySQL is ready\n"
