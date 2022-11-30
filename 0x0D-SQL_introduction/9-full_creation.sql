-- a script that creates a table second_table
-- id-INT; name-VARCHAR(256); score-INT
-- If the table already exists, script should not fail
-- NO USE select OR show
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO second_table VALUES
       (1, "John", 10),
       (2, "Alex", 3),
       (3, "Bob", 14),
       (4, "George", 8);
