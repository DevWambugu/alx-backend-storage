-- Createas a table called users
-- The script can be executed on any database
CREATE TABLE users (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	name VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE
);
