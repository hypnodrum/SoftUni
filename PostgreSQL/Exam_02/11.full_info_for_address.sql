CREATE TABLE search_results (
    id SERIAL PRIMARY KEY,
    address_name VARCHAR(50),
    full_name VARCHAR(100),
    level_of_bill VARCHAR(20),
    make VARCHAR(30),
    condition CHAR(1),
    category_name VARCHAR(50)
);

CREATE OR REPLACE PROCEDURE sp_courses_by_address (
	IN address_name VARCHAR(100)
) AS
$$
BEGIN
	TRUNCATE search_results;
	
	INSERT INTO
		search_results(
			address_name,
			full_name,
			level_of_bill,
			make,
			condition,
			category_name
		)
	SELECT 
		addresses.name,
		clients.full_name,
		CASE 
			WHEN courses.bill <= 20 THEN 'Low'
			WHEN courses.bill <= 30 THEN 'Medium'
			ELSE 'High'
		END,
		cars.make,
		cars.condition,
		categories.name
	FROM
		addresses
	JOIN 
		courses
	ON 
		addresses.id = courses.from_address_id
	JOIN
		cars
	ON 
		cars.id = courses.car_id
	JOIN 
		categories
	ON
		categories.id = cars.category_id
	JOIN 
		clients
	ON
		clients.id = courses.client_id
	WHERE 
		addresses.name = address_name
	ORDER BY
		cars.make ASC,
		clients.full_name ASC;
END;
$$
LANGUAGE plpgsql;

CALL sp_courses_by_address('700 Monterey Avenue');

SELECT * FROM search_results;
