-- Script that creates a table users with requisite requirements
-- Creates a table with unique id-nn,ai,pk; email-str(255) name-str(255)
CREATE TABLE IF NOT EXISTS users (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, email CHAR(255) NOT NULL UNIQUE, name CHAR(255));
