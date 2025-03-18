--creating Tables database
CREATE DATABASE TicketBookingSystem

--switching to Tables database 
USE TicketBookingSystem

--creating Venue Table
CREATE TABLE Venu(
	venue_id INT PRIMARY KEY NOT NULL,
	venue_name VARCHAR(50),
	address VARCHAR(200)
)

--creating Event Table
CREATE TABLE Event(
	event_id INT PRIMARY KEY NOT NULL,
	event_name VARCHAR(50),
	event_date DATE,
	event_time TIME,
	venue_id INT,
	total_seats INT,
	available_seats INT,
	ticket_price DECIMAL,
	event_type VARCHAR(50) CHECK(event_type IN ('Movie', 'Sports', 'Concert')),
	booking_id INT,
	FOREIGN KEY (venue_id) REFERENCES Venu(venue_id),
	FOREIGN KEY (booking_id) REFERENCES Booking(booking_id)
)

--creating Customer Table
CREATE TABLE Customers(
	customer_id INT PRIMARY KEY NOT NULL,
	customer_name VARCHAR(50),
	email VARCHAR(50),
	phone_number VARCHAR(20)
	booking_id INT,
	FOREIGN KEY (booking_id) REFERENCES Booking(booking_id)
)

--creating Booking Table
CREATE TABLE Booking(
	booking_id INT PRIMARY KEY NOT NULL,
	customer_id INT,
	event_id INT,
	num_tickets INT, 
	total_cost DECIMAL,
	booking_date DATETIME,
	FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
	FOREIGN KEY (event_id) REFERENCES Event(event_id), 
)

-- displaying every table created in Tables database

SELECT * FROM Venu
SELECT * FROM Event
SELECT * FROM Customers
SELECT * FROM Booking

