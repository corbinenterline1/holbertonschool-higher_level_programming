-- creates database hbtn_0d_usa & table cities
-- id unique, auto gen, not null & primay key
-- state_id INT, not null & foreign key that references to id of the states table
-- name can't be null, script shall not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id)
		REFERENCES states(id)
);
