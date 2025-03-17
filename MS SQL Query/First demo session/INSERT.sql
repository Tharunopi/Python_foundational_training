CREATE TABLE animanga(
	anime_id INT PRIMARY KEY,
	anime_name VARCHAR(50), 
	anime_mc VARCHAR(20)
)

INSERT INTO animanga(anime_id, anime_name, anime_mc)
SELECT anime_id, anime_name, anime_mc FROM anime

SELECT anime_name + 'op' AS 'ani' FROM animanga 

INSERT INTO animanga(anime_id, anime_name, anime_mc)
VALUES 
	(3, 'solo leveling', 'sun jin woo'),
	(4, 'jjk', 'yuji')