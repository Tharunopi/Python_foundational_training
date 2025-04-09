CREATE DATABASE OrderManagementSystem

USE OrderManagementSystem

CREATE TABLE Products(
	productId INT IDENTITY(1, 1) PRIMARY KEY,
	productName VARCHAR(50), 
	description VARCHAR(200),
	price FLOAT,
	quantityInStock INT, 
	type VARCHAR(20) CHECK(type IN ('Electronics', 'Clothing')),
	brand VARCHAR(20) NULL,
	warrantyPeriod INT NULL,
	size VARCHAR(10) NULL, 
	color VARCHAR(20) NULL
)

CREATE TABLE Users(
	userId INT IDENTITY(1, 1) PRIMARY KEY,
	username VARCHAR(30), 
	password VARCHAR(20), 
	role VARCHAR(10) CHECK(role IN ('Admin', 'User'))
)

CREATE TABLE Orders(
	orderId INT IDENTITY(1, 1) PRIMARY KEY,
	userId INT, 
	listOfProducts VARCHAR(MAX),
	amount FLOAT,
	FOREIGN KEY (userId) REFERENCES Users(userId)
)

SELECT * FROM Orders
SELECT * FROM Products
SELECT * FROM Users