SELECT
	first_name, last_name, make, model, mileage
FROM
	drivers AS d
JOIN
	cars_drivers AS c_d
ON c_d.driver_id = d.id

JOIN cars AS c
ON c.id = c_d.car_id
WHERE
	mileage IS NOT NULL
ORDER BY
	mileage DESC,
	first_name ASC