-- a script that lists all the cities of California

SELECT cities.id, cities.name
FROM cities
WHERE state_id=1
ORDER BY cities.id;
