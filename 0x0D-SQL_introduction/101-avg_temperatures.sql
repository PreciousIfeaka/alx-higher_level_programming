-- This script displays the average temperature in Fahrenheit by city...
-- ...ordered by temperature in descending order.
USE `hbtn_0c_0`
SELECT city, AVG(value) as `avg_temp`
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC
