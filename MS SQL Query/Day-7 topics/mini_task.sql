USE demo_assignment

SELECT * FROM marks

SELECT count(id) FROM marks
WHERE mark_1 > 80

SELECT count(id) FROM marks
WHERE mark_1 > 80 
HAVING count(id) > 2

SELECT count(id) FROM marks
WHERE mark_2 >= 80 
HAVING count(id) >= 2