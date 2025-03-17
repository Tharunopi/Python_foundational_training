--creating Tables database
CREATE DATABASE Tables

--switching to Tables database 
USE Tables

--creating Venue Table
CREATE TABLE Venu_Table(
	venue_id INT PRIMARY KEY NOT NULL,
	venue_name VARCHAR(50),
	address VARCHAR(200)
)

--creating Event Table
CREATE TABLE Event_Table(
	event_id INT PRIMARY KEY NOT NULL,
	event_name VARCHAR(50),
	event_date DATE,
	event_time TIME 
)

--altering event table because forgot to add some columns
ALTER TABLE Event_Table
ADD 
	venue_id INT,
	total_seats INT,
	available_seats INT,
	ticket_price DECIMAL,
	event_type VARCHAR(50) CHECK(event_type IN ('Movie', 'Sports', 'Concert')),
	booking_id INT,
	FOREIGN KEY (venue_id) REFERENCES Venu_Table(venue_id),
	FOREIGN KEY (booking_id) REFERENCES Booking_Table(booking_id)

--creating Customer Table
CREATE TABLE Customer_Table(
	customer_id INT PRIMARY KEY NOT NULL,
	customer_name VARCHAR(50),
	email VARCHAR(50),
	phone_number VARCHAR(20)
	--FOREIGN KEY (booking_id) REFERENCES Booking_Table(booking_id)
)

--altering table to add FK 
ALTER TABLE Customer_Table
ADD
	booking_id INT,
	FOREIGN KEY (booking_id) REFERENCES Booking_Table(booking_id)

--creating Booking Table
CREATE TABLE Booking_Table(
	booking_id INT PRIMARY KEY NOT NULL,
	customer_id INT,
	event_id INT,
	num_tickets INT, 
	total_cost DECIMAL,
	booking_date DATETIME,
	FOREIGN KEY (customer_id) REFERENCES Customer_Table(customer_id),
	FOREIGN KEY (event_id) REFERENCES Event_Table(event_id), 
)

-- displaying every table created in Tables database

SELECT * FROM Venu_Table
SELECT * FROM Event_Table
SELECT * FROM Customer_Table
SELECT * FROM Booking_Table