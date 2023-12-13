SELECT
addresses.name,

CASE
	WHEN EXTRACT(HOUR from courses.start) BETWEEN 6 AND 20 THEN 'Day'
	ELSE 'Night'
END AS day_time,
courses.bill,
clients.full_name,
cars.make,
cars.model,
categories.name AS category_name

FROM
addresses
JOIN
courses 
ON courses.from_address_id = addresses.id
JOIN
cars
ON cars.id = courses.car_id
JOIN
clients
ON clients.id = courses.client_id
JOIN
categories
ON categories.id = cars.category_id
ORDER BY courses.id