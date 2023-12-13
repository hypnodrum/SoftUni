CREATE OR REPLACE FUNCTION fn_courses_by_client(
	IN phone_num VARCHAR(20),
	OUT Output INT)

RETURNS INT as

$$
BEGIN
	Output := (SELECT
			  		COUNT(*)
			   FROM
			   	courses
			   JOIN
			   	clients
			   ON clients.id = courses.client_id
			   WHERE
			   	clients.phone_number = phone_num
			  );
END;
$$
LANGUAGE plpgsql
