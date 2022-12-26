-- creates the database 'hbtn_0d_usa' and the table 'cities' in the DB.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use the created database
USE hbtn_0d_usa;
-- creates table
CREATE TABLE IF NOT EXISTS cities (
	PRIMARY KEY(id),
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id)
	REFERENCES hbtn_0d_usa.states(id)
);
