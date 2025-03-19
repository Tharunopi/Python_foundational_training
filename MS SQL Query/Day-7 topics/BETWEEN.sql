-- These is scalar sub queries

SELECT * FROM marks 
WHERE mark_1 BETWEEN (SELECT min(mark_1) FROM marks)
AND (SELECT max(mark_1) FROM marks)

