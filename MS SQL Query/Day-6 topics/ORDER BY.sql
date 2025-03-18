USE demo_assignment

SELECT * FROM students_demo
ORDER BY name, id DESC  

SELECT TOP 1 * FROM marks
ORDER BY mark_1 DESC, mark_2 DESC 

SELECT * FROM marks 
ORDER BY mark_1 DESC, mark_2 DESC 

SELECT * FROM marks
ORDER BY mark_1 DESC, mark_2 DESC
OFFSET 2 ROWS FETCH NEXT 3 ROWS ONLY;
