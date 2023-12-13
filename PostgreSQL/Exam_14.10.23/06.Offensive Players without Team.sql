SELECT
    players.id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    age,
    position,
    salary,
    pace,
    shooting
FROM 
	players
JOIN skills_data ON skills_data.id = players.skills_data_id
WHERE 
	position = 'A'
    AND (pace + shooting) > 130
    AND players.team_id IS NULL
ORDER BY players.id;