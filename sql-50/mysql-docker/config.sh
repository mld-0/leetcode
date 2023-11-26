#!/bin/bash

# Configuration for MySQL Docker container
export CONTAINER_NAME="leetcode_sql_50"
export ROOT_PASSWORD="my-secret-pw" # This is not secure, use only for local testing
export MYSQL_IMAGE="mysql:latest"
export MYSQL_PORT="3306"

#	Should each exercise drop the database it has just created upon completion
export DROP_DATABASE_AFTER_USE="true"

