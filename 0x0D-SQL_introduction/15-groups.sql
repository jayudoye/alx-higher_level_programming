-- This script counts the number of records with a given score

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
