--  a script that lists the number of records with the same score
-- +in the second_table
-- result to display scorewith the label number
-- list sorted descending

SELECT score as "score", COUNT(score) AS "number"
FROM second_table
GROUP BY score
ORDER BY number DESC;
