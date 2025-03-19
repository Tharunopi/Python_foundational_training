USE demo_assignment

--employee(eid, ename, address, dept_id, basic_salary)
--salary(sid, eid, final_salary)

CREATE TABLE emp(
	eid INT IDENTITY(1, 1) PRIMARY KEY ,
	ename VARCHAR(20),
	dept_id INT ,
	basic_salary decimal
)

CREATE TABLE salary(
	sid INT IDENTITY(1, 1) PRIMARY KEY,
	eid INT ,
	final_salary decimal
)

INSERT INTO emp
VALUES 
	('Ajith kumar', 101, 65000),
	('Joesph Vijay', 102, 72500),
	('Rajani Kanth', 103, 58000),
	('Dhanush', 101, 61000),
	('S.T.R', 104, 79000),
	('Siva Karthikeyan', 102, 68500),
	('Chris Evans', 101, 59000),
	('Suriya', 103, 57000),
	('Vimal', 105, 85000),
	('Shiva', 102, 70000),
	('Prabas', 104, 76000),
	('Vignesh Sivan', 103, 60500),
	('M.K.Stalin', 101, 62000),
	('Rummy Nagayan', 105, 87500),
	('Kamal Hassan', 102, 69000),
	('Karthick', 104, 74500),
	('Aadhi', 103, 59500),
	('Sathiya Raj', 101, 63000),
	('Manivannan', 105, 82000),
	('Sivaji', 102, 71000);

INSERT INTO salary
VALUES 
	(1, 68250),
	(2, 75400),
	(3, 60900),
	(4, 64050),
	(5, 83740),
	(6, 71240),
	(7, 61950),
	(8, 59850),
	(9, 89250),
	(10, 73500),
	(11, 79800),
	(12, 63525),
	(13, 65100),
	(14, 92750),
	(15, 72450),
	(16, 78225),
	(17, 62475),
	(18, 66150),
	(19, 86100),
	(20, 74550);

SELECT * FROM emp
SELECT * FROM salary

--1. list the employee in each dept from employee table who gets 
--basic_salary >= avg(basic_salary) in each dept of employee
SELECT dept_id, ename, basic_salary FROM emp
WHERE basic_salary >= (SELECT avg(basic_salary) FROM emp)
GROUP BY dept_id, ename, basic_salary

--2. list the employees who gets the basic_salary >= avg(final_Salary) of the salary table
SELECT * FROM emp 
WHERE basic_salary >= (SELECT avg(final_salary) FROM salary)

--3. list the employees who gets the basic_salary >= min(final_Salary) of the salary table
SELECT * FROM emp 
WHERE basic_salary >= (SELECT min(final_salary) FROM salary)

--4. list the employees who gets the basic_salary >= max(final_Salary) of the salary table
SELECT * FROM emp 
WHERE basic_salary >= (SELECT max(final_salary) FROM salary)

--5. apply group by to display employee the basic salary details based on dep_id 
SELECT dept_id, ename, basic_salary FROM emp
GROUP BY dept_id, ename, basic_salary
ORDER BY dept_id

--6. apply group by and display the count of employee who gets the salary > 20000 by dept_id wise
SELECT dept_id, count(basic_salary) AS high_salary FROM emp
WHERE basic_salary > 20000
GROUP BY dept_id
ORDER BY dept_id

--7. co-related query: pass eid as reference outer query(employee) display the employee details with match salary table
SELECT * FROM salary 
WHERE eid IN (SELECT eid FROM emp)
