-- a script that lists all records of the table second_table
-- display score and name
-- records ordered by score

SELECT score, name
FROM second_table
WHERE score>=10
ORDER BY score DESC;
