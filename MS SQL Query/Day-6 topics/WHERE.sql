USE demo_assignment

SELECT COUNT(DISTINCT anime_name) FROM animanga

ALTER TABLE animanga
ALTER COLUMN anime_mc VARCHAR(100)

SELECT * FROM animanga


CREATE TABLE students_demo(
	id INT IDENTITY(1, 1) PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	loc VARCHAR(30)
)

INSERT INTO students_demo
VALUES 
	('Akil', 'chennai'),
	('Tharun', 'Banglore'),
	('Samutha', 'Andhra pradesh'),
	('Bipul', 'Pune'),
	('Sai Anish', 'CBE')

CREATE TABLE marks(
	id INT PRIMARY KEY,
	mark_1 INT,
	mark_2 INT,
	FOREIGN KEY (id) REFERENCES students_demo(id)
)

INSERT INTO marks
VALUES 
	(1, 90, 80),
	(2, 50, 30),
	(3, 90, 58),
	(4, 20, 30),
	(5, 100, 100)

SELECT * FROM students_demo

SELECT * FROM marks 

SELECT * FROM students_demo  
WHERE id IN (SELECT id FROM marks 
WHERE mark_1 >= 90)

-- AND OPERATOR
SELECT * FROM students_demo 
WHERE name = 'Tharun' AND loc = 'Banglore'

-- OR operator
SELECT * FROM students_demo sd
WHERE name = 'Tharun' OR loc = 'Pune'

-- BETWEEN operator
SELECT * FROM marks
WHERE id BETWEEN 2 AND 4

-- NOT operator
SELECT * FROM marks
WHERE NOT mark_1 = 90

-- LIKE operator 
SELECT * FROM students_demo
WHERE name LIKE '%l'

-- NULL & NOT NULL operator
SELECT * FROM students_demo
WHERE id IS NOT NULL 
-- always remember that empty values does not count as NULL value


SELECT * FROM students

-- Adding new DOB column
ALTER TABLE student_demo
ADD dob DATE DEFAULT '2000-01-01'