CREATE OR REPLACE FUNCTION fn_creator_with_board_games(creator_name VARCHAR(30))
RETURNS INTEGER AS 
$$
DECLARE
    total_games INTEGER;
BEGIN
    SELECT COUNT(*) INTO total_games
    FROM creators_board_games
	RIGTH JOIN creators ON creators.id = RIGTH.creator_id
    WHERE creators.first_name = creator_name;
    RETURN total_games;
END;
$$
LANGUAGE plpgsql;

--SELECT fn_creator_with_board_games('Bruno')



