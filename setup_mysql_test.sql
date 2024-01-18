-- Script setup for MySQL server for the project

-- Create database `hbnb_test_db`
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user `hbnb_test@host`
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant database privileges to user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance schema to user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;
