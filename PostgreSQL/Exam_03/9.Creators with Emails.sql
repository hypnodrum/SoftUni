SELECT 
	CONCAT(creators.first_name, ' ', creators.last_name) AS full_name,
	creators.email,
	MAX(board_games.rating) as rating
FROM 
	creators
JOIN 
	creators_board_games ON creators.id = creators_board_games.creator_id
JOIN 
	board_games ON creators_board_games.board_game_id = board_games.id
WHERE
	creators.email LIKE '%.com'
GROUP BY 
	full_name, creators.email
ORDER BY
	full_name