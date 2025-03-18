SELECT * FROM students_demo

ALTER TABLE students_demo
ADD dob DATE DEFAULT '2000-01-01'

UPDATE students_demo 
SET dob = '2000-01-01'
WHERE dob IS NULL 

UPDATE students_demo
SET dob = '2003-11-26'

UPDATE students_demo
SET dob = '2003-12-26'
WHERE name IN ('Tharun') OR name LIKE 'B____'

