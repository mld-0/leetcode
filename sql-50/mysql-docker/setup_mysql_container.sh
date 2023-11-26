#!/bin/bash

# Source common configuration
source "$(dirname "$0")/config.sh"

echo "Pull MySQL Image:"
docker pull $MYSQL_IMAGE 
echo ""

echo "Run MySQL Container:"
docker run --name $CONTAINER_NAME -e MYSQL_ROOT_PASSWORD=$ROOT_PASSWORD -d -p $MYSQL_PORT:$MYSQL_PORT $MYSQL_IMAGE
echo ""

