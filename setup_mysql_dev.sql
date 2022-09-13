-- Script that prepares a MySQL server

-- New database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- New user hbnb_dev in localhost
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

-- grant all privileges on the database to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost';

-- grant hbnb_dev SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.*
TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
