SELECT
	board_games.id AS id,
	board_games.name AS name,
	board_games.release_year AS release_year,
	categories.name AS category_name
FROM
	board_games
JOIN
 	categories ON categories.id = board_games.category_id
WHERE
	categories."name" = CONCAT('Strategy',' ', 'Games') OR categories."name" = 'Wargames'
ORDER BY release_year DESC