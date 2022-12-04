-- a script that creates MySQL user_0d_1
-- user has all privileges
-- user has password user_0d_1_pwd
-- if user exit script no fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
