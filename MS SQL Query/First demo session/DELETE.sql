INSERT INTO anime(anime_id, anime_name, anime_mc)
VALUES 
	(3, 'solo leveling', 'sun jin woo'),
	(4, 'jjk', 'yuji')

DELETE FROM anime 
WHERE anime_mc = 'yuji' AND anime_name = 'jjk'

SELECT * FROM anime