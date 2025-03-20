create TABLE emp_loan(
	loan_id INT IDENTITY(1, 1) PRIMARY KEY,
	eid INT ,
	sid INT ,
	loan_amt DECIMAL(10, 2)
)

INSERT INTO emp_loan
VALUES 
	(20, 20, 99999),
	(4, 4, 29849),
	(12, 12, 78473)

SELECT * FROM emp e
SELECT * FROM salary s

SELECT * FROM emp e
RIGHT JOIN salary s
ON s.eid = e.eid

SELECT e.dept_id, count(s.sid) AS count FROM emp e
INNER JOIN salary s
ON s.eid = e.eid
GROUP BY e.dept_id
HAVING count(s.sid) = 3

SELECT e.dept_id, e.ename, s.final_salary FROM emp e
LEFT OUTER JOIN salary s
ON s.eid = e.eid
GROUP BY e.dept_id, e.ename, s.final_salary

-- JOINS with multiple table
-- LEFT JOIN
SELECT s.eid, s.final_salary, e.ename, l.loan_amt FROM salary s
LEFT JOIN emp e
ON e.eid = s.eid
LEFT JOIN emp_loan l
ON s.eid = l.eid

--RIGHT JOIN
SELECT s.eid, s.final_salary, l.loan_amt FROM emp e
RIGHT JOIN salary s
ON s.eid = e.eid
RIGHT JOIN emp_loan l
ON s.eid = l.eid
ORDER BY s.final_salary DESC 