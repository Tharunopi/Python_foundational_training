USE demo_assignment

CREATE TABLE students(
	id INT,
	name VARCHAR(50),
)

INSERT INTO students
VALUES
	(1, 'Tharun'), 
	(2, 'Aadhi')

SELECT * FROM students 
WHERE name = 'Aadhi'
