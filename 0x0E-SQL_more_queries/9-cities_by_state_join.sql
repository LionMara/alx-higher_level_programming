-- a script that lists all cities
-- display: cities.id - cities.name - states.name
-- one SELECT statement

SELECT cities.id AS 'id',
       cities.name AS 'name',
       states.name AS 'name'
FROM states, cities
WHERE cities.state_id = states.id
ORDER BY cities.id;
