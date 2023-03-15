-- Creates a table that has id INT with default value 1 and must be unique
-- The database name will be passed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256));
