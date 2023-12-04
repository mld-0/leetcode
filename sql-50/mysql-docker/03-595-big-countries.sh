#!/bin/bash

source "$(dirname "$0")/config.sh"
SCRIPT_BASENAME=$(basename "$0" .sh)
DB_NAME="${SCRIPT_BASENAME//-/_}" 

read -r -d '' SQL_EXERCISE_QUERY <<EOSQL
SELECT name, population, area FROM World WHERE area >= 3000000 OR population >= 25000000;
EOSQL

read -r -d '' SQL_CREATE_DB <<EOSQL
CREATE DATABASE IF NOT EXISTS \`$DB_NAME\`;
EOSQL

read -r -d '' SQL_FILL_DB <<EOSQL
CREATE TABLE World (
    name VARCHAR(255) PRIMARY KEY,
    continent VARCHAR(255),
    area INT,
    population INT,
    gdp BIGINT
);
INSERT INTO World (name, continent, area, population, gdp) VALUES
('Afghanistan', 'Asia', 652230, 25500100, 20343000000),
('Albania', 'Europe', 28748, 2831741, 12960000000),
('Algeria', 'Africa', 2381741, 37100000, 188681000000),
('Andorra', 'Europe', 468, 78115, 3712000000),
('Angola', 'Africa', 1246700, 20609294, 100990000000);
EOSQL

read -r -d '' SQL_SHOW_TABLE <<EOSQL
SELECT * FROM World;
EOSQL

read -r -d '' SQL_SELECT_DB <<EOSQL
USE \`$DB_NAME\`;
EOSQL

SQL_DROP_DB=$([ "$DROP_DATABASE_AFTER_USE" = true ] && echo "DROP DATABASE IF EXISTS \`$DB_NAME\`;")

#	Run Commands:
OUTPUT=`
docker exec -i -e MYSQL_PWD="$ROOT_PASSWORD" $CONTAINER_NAME mysql -u root -t <<EOF 
$SQL_CREATE_DB
$SQL_SELECT_DB
$SQL_FILL_DB
$SQL_SHOW_TABLE
$SQL_SELECT_DB
$SQL_EXERCISE_QUERY
$SQL_DROP_DB
EOF
`

#	Print Output:
echo_sql 	"$SQL_CREATE_DB" 
echo_sql 	"$SQL_FILL_DB" 
echo_sql 	"$SQL_SHOW_TABLE" 
echo_sql 	"$SQL_EXERCISE_QUERY" 
echo_sql 	"$SQL_DROP_DB" 
echo 		"$OUTPUT"

