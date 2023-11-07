#!/bin/bash

# Source common configuration
source "$(dirname "$0")/config.sh"

# Pull the latest MySQL image
docker pull $MYSQL_IMAGE

# Run the MySQL container
docker run --name $CONTAINER_NAME -e MYSQL_ROOT_PASSWORD=$ROOT_PASSWORD -d -p $MYSQL_PORT:$MYSQL_PORT $MYSQL_IMAGE

