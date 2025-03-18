USE demo_assignment

SELECT * FROM marks

SELECT sum(mark_1) AS sum_mark_1, sum(mark_2) AS sum_mark_2 FROM marks

SELECT avg(mark_1) AS avg_m1, avg(mark_2) AS avg_m2 FROM marks

SELECT min(mark_1) AS min_1, min(mark_2) AS min_2 FROM marks

SELECT max(mark_1) AS max_1, max(mark_2) AS max_2 FROM marks

SELECT avg(mark_1) + avg(mark_2) AS avg_m2 FROM marks

SELECT anime_name, avg(anime_id) AS anime_id_avg FROM animanga
GROUP BY anime_name
HAVING avg(anime_id) BETWEEN 10 AND 48
ORDER BY avg(anime_id) DESC

SELECT name FROM students_demo
WHERE id IN (
SELECT id FROM marks
GROUP BY id
HAVING (avg(mark_1) + avg(mark_2))/2 > 50
)

SELECT name FROM sys.databases 
