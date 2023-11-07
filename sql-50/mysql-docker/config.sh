#!/bin/bash

# Configuration for MySQL Docker container
export CONTAINER_NAME="temp_mysql"
export ROOT_PASSWORD="my-secret-pw" # This is not secure, use only for local testing
export MYSQL_IMAGE="mysql:latest"
export MYSQL_PORT="3306"
