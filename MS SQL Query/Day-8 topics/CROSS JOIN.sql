CREATE TABLE tb1(
	val VARCHAR(3)
)

CREATE TABLE tb2(
	color VARCHAR(10)
	)

INSERT INTO tb1
VALUES 
	('A'),
	('B')

INSERT INTO tb2
VALUES 
	('black'),
	('white')

SELECT * FROM tb1
CROSS JOIN tb2