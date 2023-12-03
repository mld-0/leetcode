#!/bin/bash

source "$(dirname "$0")/config.sh"
SCRIPT_BASENAME=$(basename "$0" .sh)
DB_NAME="${SCRIPT_BASENAME//-/_}" 

read -r -d '' SQL_EXERCISE_QUERY <<EOSQL
SELECT product_id FROM Products WHERE low_fats = 'Y' AND recyclable = 'Y';
EOSQL

read -r -d '' SQL_CREATE_DB <<EOSQL
CREATE DATABASE IF NOT EXISTS \`$DB_NAME\`;
EOSQL

read -r -d '' SQL_FILL_DB <<EOSQL
CREATE TABLE IF NOT EXISTS Products (product_id INT, low_fats CHAR(1), recyclable CHAR(1));
INSERT INTO Products VALUES (0, 'Y', 'N'), (1, 'Y', 'Y'), (2, 'N', 'Y'), (3, 'Y', 'Y'), (4, 'N', 'N');
EOSQL

read -r -d '' SQL_SHOW_TABLE <<EOSQL
SELECT * FROM Products;
EOSQL

read -r -d '' SQL_SELECT_DB <<EOSQL
USE \`$DB_NAME\`;
EOSQL

SQL_DROP_DB=$([ "$DROP_DATABASE_AFTER_USE" = true ] && echo "DROP DATABASE IF EXISTS \`$DB_NAME\`;")

#	Create and fill DB:
OUTPUT_CREATE_DB=`
docker exec -i -e MYSQL_PWD="$ROOT_PASSWORD" $CONTAINER_NAME mysql -u root --table <<EOF 
$SQL_CREATE_DB
$SQL_SELECT_DB
$SQL_FILL_DB
$SQL_SHOW_TABLE
EOF
`

#	Run Exercise Query:
OUTPUT_EXERCISE_QUERY=`
docker exec -i -e MYSQL_PWD="$ROOT_PASSWORD" $CONTAINER_NAME mysql -u root --table <<EOF 
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
echo "$SCRIPT_BASENAME:"
echo "$SQL_CREATE_DB" | sed "s/^/>>/g"
echo "$SQL_FILL_DB" | sed "s/^/>>/g"
echo "$SQL_SHOW_TABLE" | sed "s/^/>>/g"
echo "$OUTPUT_CREATE_DB"
echo "$SQL_EXERCISE_QUERY" | sed "s/^/>>/g"
echo "$OUTPUT_EXERCISE_QUERY"
echo "$SQL_DROP_DB" | sed "s/^/>>/g"
echo ""

