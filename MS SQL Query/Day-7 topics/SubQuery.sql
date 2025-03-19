SELECT * FROM marks m

-- sub-quries are working independentely are called Non-Correlation quries
SELECT * FROM students_demo
WHERE id IN (SELECT id FROM marks
			 WHERE mark_1 BETWEEN 0 AND 75) 

SELECT id, name, loc FROM students_demo
WHERE Id IN (SELECT id FROM marks
			WHERE mark_1 >= 60)

SELECT id, name, loc FROM students_demo
WHERE Id NOT IN (SELECT id FROM marks
			WHERE mark_1 >= 60)

SELECT * FROM students_demo sd
WHERE EXISTS (SELECT 1 from marks WHERE mark_1 >= 90)

--sub-quries are not working independentely are called Correlation quries
SELECT * FROM students_demo sd
WHERE NOT EXISTS (SELECT 'bankai' FROM marks m
				   WHERE m.id = sd.id 
				   AND mark_1 >= 90)