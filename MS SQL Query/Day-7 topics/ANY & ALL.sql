USE demo_assignment;

-- ANY - return true if any one of the values satisfies the condition
SELECT * FROM marks m
WHERE m.mark_1 >= ANY (SELECT max(mark_1) 
					   FROM marks m)

SELECT mark_1, count(id) FROM marks m
GROUP BY mark_1

SELECT * FROM employee e
WHERE salary > ANY (SELECT salary FROM employee e1)

SELECT * FROM employee e
WHERE NOT salary > ANY (SELECT salary FROM employee e1)

-- ALL 
SELECT * FROM employee e
WHERE salary >= ALL (SELECT salary FROM employee e1)

SELECT * FROM employee e
WHERE NOT salary >= ALL (SELECT salary FROM employee e1)