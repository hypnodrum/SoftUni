SELECT
	full_name, 
	COUNT(car_id) as count_of_cars,
	SUM(bill) AS total_sum
FROM
clients
JOIN courses ON courses.client_id = clients.id
WHERE full_name LIKE '_a%' 
GROUP BY clients.full_name
HAVING COUNT(car_id) > 1
ORDER BY clients.full_name


	