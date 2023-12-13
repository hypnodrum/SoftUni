SELECT
    teams.id AS team_id,
    teams.name AS team_name,
    COUNT(players.id) AS player_count,
    teams.fan_base AS fan_base
FROM teams
LEFT JOIN players ON teams.id = players.team_id
GROUP BY 
	teams.id, teams.name, teams.fan_base
HAVING 
	teams.fan_base > 30000
ORDER BY 
	player_count DESC, 
	teams.fan_base DESC;