SELECT anime_name, anime_mc FROM (SELECT * FROM animanga )a

SELECT * FROM (SELECT TOP 3 id, mark_1 from marks m
				ORDER BY mark_2) AS m
ORDER BY mark_1 DESC

SELECT id, avg(mark_1), avg(mark_2) AS average FROM (
													SELECT TOP 3 id, mark_1, mark_2 FROM marks
													) AS m
GROUP BY id