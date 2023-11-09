#!/bin/bash

# Source common configuration
source "$(dirname "$0")/config.sh"

echo "Cleanup container:"

# Stop the MySQL container
docker stop $CONTAINER_NAME

# Remove the MySQL container
docker rm $CONTAINER_NAME

