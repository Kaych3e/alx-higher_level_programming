-- Lists all records of the table second_table with name value
-- Records are listed by descending score
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
