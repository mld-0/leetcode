#!/bin/bash

# Load common configuration
source "$(dirname "$0")/config.sh"

# Execute commands within the MySQL Docker container
docker exec -i $CONTAINER_NAME mysql -u root -p$ROOT_PASSWORD <<EOF
CREATE DATABASE IF NOT EXISTS exercise_db;
USE exercise_db;

CREATE TABLE IF NOT EXISTS Products (product_id INT, low_fats CHAR(1), recyclable CHAR(1));
INSERT INTO Products VALUES (0, 'Y', 'N'), (1, 'Y', 'Y'), (2, 'N', 'Y'), (3, 'Y', 'Y'), (4, 'N', 'N');

-- Display the table
SELECT * FROM Products;

-- Execute the query
SELECT product_id FROM Products WHERE low_fats = 'Y' AND recyclable = 'Y';

-- Clean up: drop the database
DROP DATABASE exercise_db;
EOF

