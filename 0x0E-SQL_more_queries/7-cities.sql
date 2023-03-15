-- Creates a database 'hbtn_0d_usa' and the table 'cities'
-- id INT unique, auto generated, cant be null and is a primary key
-- state_id INT, cant be null and must be a FOREIGN KEY that references to id of the 'states' table
-- name VARCHAR(256) cant be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
(
 	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id)
		REFERENCES hbtn_0d_usa.states(id)
);
