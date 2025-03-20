USE demo_assignment

SELECT ascii('a') AS ascii_values

SELECT char(97) 

SELECT charindex('n', 'Tharun Atithya') AS position

SELECT ename + ' hi' FROM emp e

SELECT ltrim('       ki') AS string

SELECT rtrim('ki             ') AS string

SELECT len('Tharun') AS str_len

SELECT DATALENGTH('Tharun') AS str_len

-- difference of the strings 

SELECT DIFFERENCE('Tharun', 'tharun') AS difference

SELECT ename, DIFFERENCE(ename, 'tharun') FROM emp
WHERE DIFFERENCE(ename, 'kamal hassan') >= 3

SELECT LEFT('Tharun Atithya', 6) AS name

SELECT RIGHT('Tharun Atithya', 7) AS name

SELECT ename, LEN(ename) AS name_length FROM emp 
WHERE LEN(ename) > 6
ORDER BY LEN(ename)

SELECT ename, LOWER(ename) AS lower, UPPER(ename) AS upper FROM emp

SELECT ename, REPLACE(ename, 'A', 'Z') FROM emp

SELECT REVERSE(REPLACE(ename, 'A', 'Z')) FROM emp

SELECT SUBSTRING(REVERSE(REPLACE(ename, 'A', 'Z')), 2, 6) AS sub_string FROM emp

