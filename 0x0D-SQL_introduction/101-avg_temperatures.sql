-- This script shows average temperature by city from table temperatures

SELECT city, AVG(value)
AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
