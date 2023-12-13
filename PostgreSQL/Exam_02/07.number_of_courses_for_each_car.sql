SELECT
	cars.id as car_id,
	make,
	mileage,
	COUNT(courses.id) AS count_of_courses,
	ROUND(AVG(courses.bill),2) AS average_bill
	
FROM cars
left JOIN courses ON courses.car_id = cars.id

GROUP BY 
	cars.id
HAVING COUNT(courses.id) <> 2
ORDER BY
	count_of_courses DESC,
	cars.id
	