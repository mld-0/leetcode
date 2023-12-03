#!/bin/bash

source "$(dirname "$0")/config.sh"
SCRIPT_BASENAME=$(basename "$0" .sh)
DB_NAME="${SCRIPT_BASENAME//-/_}" 

read -r -d '' SQL_EXERCISE_QUERY <<EOSQL
SELECT name FROM Customer WHERE referee_id != 2 OR referee_id IS NULL
EOSQL

read -r -d '' SQL_CREATE_DB <<EOSQL
CREATE DATABASE IF NOT EXISTS \`$DB_NAME\`;
EOSQL

read -r -d '' SQL_FILL_DB <<EOSQL
CREATE TABLE Customer (
    id INT,
    name VARCHAR(255),
    referee_id INT
);
INSERT INTO Customer (id, name, referee_id) VALUES 
(1, 'Will', NULL),
(2, 'Jane', NULL),
(3, 'Alex', 2),
(4, 'Bill', NULL),
(5, 'Zack', 1),
(6, 'Mark', 2);
EOSQL

read -r -d '' SQL_SHOW_TABLE <<EOSQL
SELECT * FROM Customer;
EOSQL

read -r -d '' SQL_SELECT_DB <<EOSQL
USE \`$DB_NAME\`;
EOSQL

SQL_DROP_DB=$([ "$DROP_DATABASE_AFTER_USE" = true ] && echo "DROP DATABASE IF EXISTS \`$DB_NAME\`;")

#	Create and fill DB:
OUTPUT_CREATE_DB=`
docker exec -i -e MYSQL_PWD="$ROOT_PASSWORD" $CONTAINER_NAME mysql -u root -t <<EOF 
$SQL_CREATE_DB
$SQL_SELECT_DB
$SQL_FILL_DB
$SQL_SHOW_TABLE
EOF
`

#	Run Exercise Query:
OUTPUT_EXERCISE_QUERY=`
docker exec -i -e MYSQL_PWD="$ROOT_PASSWORD" $CONTAINER_NAME mysql -u root -t <<EOF 
$SQL_SELECT_DB
$SQL_EXERCISE_QUERY
EOF
`

#	Drop DB:
OUTPUT_DROP_DB=`
docker exec -i -e MYSQL_PWD="$ROOT_PASSWORD" $CONTAINER_NAME mysql -u root <<EOF
$SQL_DROP_DB
EOF
`

#	Print Output:
echo_sql 	"$SQL_CREATE_DB" 
echo_sql 	"$SQL_FILL_DB" 
echo_sql 	"$SQL_SHOW_TABLE" 
echo 		"$OUTPUT_CREATE_DB"
echo_sql 	"$SQL_EXERCISE_QUERY" 
echo 		"$OUTPUT_EXERCISE_QUERY"
echo_sql 	"$SQL_DROP_DB" 

