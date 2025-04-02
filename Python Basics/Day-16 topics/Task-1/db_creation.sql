CREATE DATABASE ecom

USE ecom

CREATE TABLE customer(
	cid INT PRIMARY KEY,
	cname VARCHAR(50), 
	address VARCHAR(150),
	mob VARCHAR(15)
)

CREATE TABLE product(
	pid INT PRIMARY KEY, 
	pname varchar(50),
	descri VARCHAR(200),
	price FLOAT
)

CREATE TABLE orders(
	oid INT PRIMARY KEY,
	date VARCHAR(25), 
	cid INT,
	pid INT,
	qty INT, 
	price FLOAT, 
	total_amount FLOAT,
	FOREIGN KEY(cid) REFERENCES customer(cid),
	FOREIGN KEY(pid) REFERENCES product(pid)
)

SELECT * FROM customer 
SELECT * FROM product 
SELECT * FROM orders 