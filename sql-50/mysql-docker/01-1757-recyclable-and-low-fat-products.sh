#!/bin/bash

source "$(dirname "$0")/config.sh"

SCRIPT_BASENAME=$(basename "$0" .sh)
DB_NAME="${SCRIPT_BASENAME//-/_}"
DB_NAME="${DB_NAME//[^a-zA-Z0-9_]/}"

echo "$SCRIPT_BASENAME"

DROP_DB_COMMAND=""
if [ "$DROP_DATABASE_AFTER_USE" = true ]; then
  DROP_DB_COMMAND="DROP DATABASE IF EXISTS \`$DB_NAME\`;"
fi

docker exec -i $CONTAINER_NAME mysql -u root -p$ROOT_PASSWORD <<EOF
CREATE DATABASE IF NOT EXISTS \`$DB_NAME\`;
USE \`$DB_NAME\`;

CREATE TABLE IF NOT EXISTS Products (product_id INT, low_fats CHAR(1), recyclable CHAR(1));
INSERT INTO Products VALUES (0, 'Y', 'N'), (1, 'Y', 'Y'), (2, 'N', 'Y'), (3, 'Y', 'Y'), (4, 'N', 'N');

-- Display the table
SELECT * FROM Products;

-- Execute the query
SELECT product_id FROM Products WHERE low_fats = 'Y' AND recyclable = 'Y';

-- Clean up: drop the database if the flag is set
$DROP_DB_COMMAND
EOF

echo ""
