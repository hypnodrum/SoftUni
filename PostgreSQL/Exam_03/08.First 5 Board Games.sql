SELECT 
	board_games.name,
	board_games.rating,
	categories.name AS category_name
FROM 
   	board_games
JOIN 
	categories ON categories.id = board_games.category_id
JOIN
	players_ranges ON players_ranges.id = board_games.players_range_id
WHERE
	(rating > 7.00 AND (board_games.name ILIKE '%a%' OR rating > 7.50)) 
	AND (players_ranges.min_players BETWEEN 2 AND 5 AND players_ranges.max_players BETWEEN 2 and 5)
ORDER BY
	board_games.name ASC,
	rating DESC
LIMIT 5	