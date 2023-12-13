DELETE FROM board_games
WHERE id IN (
    SELECT
        bg.id
    FROM
        board_games AS bg
    JOIN publishers AS p ON bg.publisher_id = p.id
    JOIN addresses AS a on p.address_id = a.id
    WHERE a.town LIKE('L%')
);
 
DELETE FROM publishers
WHERE id IN (
    SELECT
        p.id
    FROM
        publishers AS p
    JOIN addresses AS a on p.address_id = a.id
    WHERE a.town LIKE('L%')
);
 
DELETE FROM addresses
WHERE town LIKE('L%');