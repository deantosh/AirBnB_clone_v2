-- Script prepare MySQL server for the project

-- create database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create user if not exists
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant a privileges on the database to user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- grant select privilege on the database performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost'; 

-- flush privieges to apply changes
FLUSH PRIVILEGES;
