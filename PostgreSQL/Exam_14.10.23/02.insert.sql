INSERT INTO coaches (first_name, last_name, salary, coach_level)
SELECT
	players.first_name AS firs_name,
	players.last_name AS last_name,
	players.salary * 2 AS salary,
	LENGTH(players.first_name) AS coach_level
FROM players
WHERE hire_date < '2013-12-13 07:18:46';