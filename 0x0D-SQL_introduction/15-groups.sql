--Lists the number of records with the same score in the table second_table
--Result displays: score, number of records for this score with label number
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
