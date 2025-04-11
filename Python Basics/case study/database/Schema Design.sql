USE Car_rental_application

-- Vehicle Table
CREATE TABLE Vechile_Table(
	vechileID INT PRIMARY KEY,
	make VARCHAR(50),
	model VARCHAR(50),
	year DATE, 
	dailyRate DECIMAL,
	status VARCHAR(20) CHECK(status IN ('available', 'notAvailable')),
	passengerCapacity INT,
	engineCapacity DECIMAL
)

-- Customer Table
CREATE TABLE Customer_Table(
	customerID INT PRIMARY KEY,
	firstName VARCHAR(50),
	lastName VARCHAR(50),
	email VARCHAR(200),
	phoneNumber VARCHAR(20)
)

-- Lease Table
CREATE TABLE Lease_Table(
	leaseID INT PRIMARY KEY,
	vehileID INT,
	customerID INT,
	startDate DATE,
	endDate DATE,
	type VARCHAR(20) CHECK(type IN ('DailyLease', 'MonthlyLease'))
	FOREIGN KEY (vehileID) REFERENCES Vechile_Table(vechileID),
	FOREIGN KEY (customerID) REFERENCES Customer_Table(customerID)
)

-- Payment Table 
CREATE TABLE Payment_Table(
	paymentID INT PRIMARY KEY,
	leaseID INT,
	paymentDate DATETIME,
	amount DECIMAL,
	FOREIGN KEY (leaseID) REFERENCES Lease_Table(leaseID)
)

SELECT * FROM Vechile_Table
SELECT * FROM Customer_Table 
SELECT * FROM Lease_Table
SELECT * FROM Payment_Table
