SELECT
 	creators.last_name,
 	ceil(board_games.rating) AS average_rating,
 	publishers.name AS publisher_name
FROM
	creators
JOIN
	creators_board_games ON creators_board_games.creator_id = creators.id
JOIN
	board_games ON board_games.id = creators_board_games.board_game_id
JOIN
	publishers ON publishers.id = board_games.publisher_id
WHERE
	publishers.name = 'Stonemaier Games'
ORDER BY
	rating DESC
