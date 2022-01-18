SELECT a.cust_name AS "city", 
a.city, b.commission 
FROM customer a 
INNER JOIN salesman b 
ON a.salesman_id=b.salesman_id 
WHERE b.commission>.10;