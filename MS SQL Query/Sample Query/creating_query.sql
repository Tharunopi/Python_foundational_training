create table employee(
	id INT IDENTITY(1, 1) PRIMARY KEY, 
	name VARCHAR(20) NOT NULL
)

ALTER TABLE employee 
	ADD age INT 
	
INSERT INTO employee
VALUES
	('Tharun')

INSERT INTO employee
VALUES 
	('Tharun', 21)

SELECT * FROM employee 
WHERE age = 21