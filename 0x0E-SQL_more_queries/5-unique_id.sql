-- a script that creates the table unique_id
-- not nullwith default val 1 and must be unique(id-INT)
-- name-VARCHAR(256) NOT NULL
CREATE TABLE IF NOT EXISTS unique_id
       (id INT UNIQUE DEFAULT 1, name VARCHAR(256) NOT NULL);
