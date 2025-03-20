USE demo_assignment

INSERT INTO salary
VALUES
	(21, 200000),
	(99, 98453)

UPDATE salary
SET 
	final_salary = NULL 
	WHERE eid BETWEEN 15 AND 20

SELECT * FROM emp
SELECT * FROM salary s

--INNER JOIN
SELECT e.dept_id, e.eid, e.ename, s.final_salary FROM emp e
INNER JOIN salary s
ON s.eid = e.eid
WHERE s.final_salary >= 70000

-- LEFT JOIN
SELECT * FROM salary s
LEFT JOIN emp e
ON e.eid = s.eid

--RIGHT JOIN 
SELECT * FROM emp e
RIGHT JOIN salary s
ON s.eid = e.eid
