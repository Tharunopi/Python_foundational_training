USE demo_assignment

SELECT * FROM animanga 

SELECT name, count(dob) FROM students_demo 
GROUP BY name

CREATE TABLE employee(
	id INT IDENTITY(1, 1) PRIMARY key,
	name varchar(20),
	dept_id INT,
	salary DECIMAL
)

INSERT INTO employee
VALUES 
	('Anish', 101, 20000),
	('Yadav', 102, 50000),
	('Vinoth', 103, 60000),
	('Kumar', 101, 20000),
	('Santhosh', 102, 45000),
	('Rajesh', 101, 50000)

SELECT dept_id, count(dept_id) FROM employee 
GROUP BY dept_id

SELECT dept_id, count(name) AS employee FROM employee 
WHERE salary >= 50000
GROUP BY dept_id

SELECT dept_id, count(name) AS employee FROM employee
GROUP BY dept_id
HAVING avg(salary) > 30000

SELECT dept_id, avg(salary) AS average_salary FROM employee
GROUP BY dept_id
HAVING avg(salary) > 45000

SELECT dept_id, count(name) AS emp_count FROM employee
GROUP BY dept_id
HAVING count(name) >= 2