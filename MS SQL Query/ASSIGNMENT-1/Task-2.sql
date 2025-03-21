USE TicketBookingSystem

--1. Write a SQL query to insert at leat 10 sample records into each table.

--venu table
INSERT INTO Venu
VALUES 
	(1, 'Hotel Gagan Plaza', 'Kanpur city'),
	(2, 'Mandakini Heaven Huts', 'South of Kanpur'),
	(3, 'Rainforest Retreats Pvt Ltd', 'Saleshpur'),
	(4, 'Viveda Wellness Village', 'Nashik'),
	(5, 'Ahinsa Residency', 'Gurugram'),
	(6, 'Serieti', 'Soul Society'),
	(7, 'Leaf village', 'Ohio'),
	(8, 'Shiganshina', 'Paradi island'),
	(9, 'J-World Tokyo', 'Tokyo'),
	(10, 'Chennai Trade Centre', 'Chennai')

--booking table 
 INSERT INTO Booking 
 VALUES
	(1, 1, 1, 2, 90.00, '2025-03-25'),
	(2, 2, 3, 4, 300.00, '2025-03-26'),
	(3, 3, 2, 5, 150.00, '2025-03-27'),
	(4, 4, 4, 3, 45.00, '2025-03-28'),
	(5, 5, 5, 2, 20.00, '2025-03-29'),
	(6, 6, 6, 6, 150.00, '2025-03-30'),
	(7, 7, 7, 4, 48.00, '2025-04-01'),
	(8, 8, 8, 1, 100.00, '2025-04-02'),
	(9, 9, 9, 10, 350.00, '2025-04-03'),
	(10, 10, 10, 5, 100.00, '2025-04-04');

--customer table

INSERT INTO Customers
VALUES
	(1, 'Ajith Kumar', 'thala@example.com', '9865551234', 5),
	(2, 'Joesph Vijay', 'tvkvijay@example.com', '7845552345', 4),
	(3, 'Mohan Ravi', 'jayamravi@example.com', '9665553456', 3),
	(4, 'Dhanush', 'dkraja@example.com', '9995554567', 2),
	(5, 'Suriya', 'suriya@example.com', '9475555678', 1),
	(6, 'Karthick', 'dili@example.com', '9265556789', 10),
	(7, 'Vimal', 'supremestar@example.com', '9365557890', 9),
	(8, 'Prithiv Raj', 'goatlife@example.com', '8305558901', 8),
	(9, 'Pream', 'pream@example.com', '9875559012', 7),
	(10, 'RajiniKanth', 'eagle@example.com', '6875550123',6);

--event table
INSERT INTO Event 
VALUES
	(1, 'Audio Launch', '2025-04-15', '19:00', 1, 500, 500, 45.00, 'Movie', 1),
	(2, 'Kabbadi Championship', '2025-04-20', '14:00', 2, 10000, 10000, 30.00, 'Sports', 9),
	(3, 'Music Orchestra', '2025-05-01', '20:00', 3, 300, 300, 75.00, 'Concert', 10),
	(4, 'Avengers Reloaded', '2025-04-10', '18:00', 4, 200, 200, 15.00, 'Movie', 7),
	(5, 'Art Exhibition', '2025-05-05', '10:00', 9, 150, 150, 10.00, 'Concert', 8),
	(6, 'Tennis Tournament', '2025-05-10', '13:00', 6, 5000, 5000, 25.00, 'Sports', 6),
	(7, 'University Play', '2025-04-25', '19:30', 7, 250, 250, 12.00, 'Movie', 5),
	(8, 'Tech Conference', '2025-06-01', '09:00', 8, 1000, 1000, 100.00, 'Concert', 4),
	(9, 'Cricket Game', '2025-05-15', '15:00', 6, 12000, 12000, 35.00, 'Sports', 3),
	(10, 'Pongal Festival', '2025-06-15', '12:00', 10, 2000, 2000, 20.00, 'Concert', 2);

--2. Write a SQL query to list all Events
SELECT DISTINCT(event_name) AS Events FROM Event 

--3. Write a SQL query to select events with available tickets.
SELECT event_name AS available_tickets FROM Event 
WHERE available_seats >= 1

--4. Write a SQL query to select events name partial match with 'cup'
SELECT event_name AS Events FROM Event 
WHERE event_name LIKE '%cup%'

--5. Write a SQL query to select events with ticket price range is between 1000 to 2500
SELECT event_name AS Events FROM Event 
WHERE ticket_price BETWEEN 1000 AND 2500

--6. Write a SQL query to retrieve events with dates falling within a specific range
SELECT event_name, event_date FROM Event 
WHERE event_date BETWEEN '2025-04-01' AND '2025-04-30'

--7. Write a SQL Query to retrieve events with available tickets that also have 'Concert' in their name.
SELECT event_name AS Concert_Events, available_seats FROM Event
WHERE event_type = 'Concert' AND available_seats >= 1

--8. Write a SQL query to retrieve users in batches of 5, starting from the 6th user
SELECT customer_name AS Batch_Users FROM Customers 
ORDER BY customer_id ASC 
OFFSET 5 ROWS FETCH NEXT 5 ROWS ONLY 

--9. Write a SQL query to retrieve bookings details contains booked no of ticket more than 4.
SELECT * FROM Booking 
WHERE num_tickets > 4

--10. Write a SQL query to retrieve customer information whose phone number end with '000'
SELECT * FROM Customers 
WHERE phone_number LIKE '%000'

--11. Write a SQL query to retrieve the events in order whose seat capacity more than 15000.
SELECT event_name AS Events FROM Event 
WHERE total_seats > 15000

--12. Write a SQL query to select events name not start with 'x', 'y', 'z'.
SELECT event_name AS Events FROM Event
WHERE event_name NOT LIKE 'x%' 
AND event_name NOT LIKE 'y%' 
AND event_name NOT LIKE 'z%'

