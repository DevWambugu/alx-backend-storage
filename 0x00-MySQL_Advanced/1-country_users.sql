-- Createas a table called users with the named
-- columns
-- The script can be executed on any database
CREATE TABLE users (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	name VARCHAR(255),
	email VARCHAR(255) NOT NULL UNIQUE,
	country country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
