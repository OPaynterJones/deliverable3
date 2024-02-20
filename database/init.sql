CREATE TABLE `events`(
    `event_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `society_id` BIGINT NOT NULL,
    `name` TINYTEXT NOT NULL,
    `description` TEXT NULL,
    `datetime` DATETIME NOT NULL,
    `location` TINYTEXT NOT NULL,
    `picture` TINYTEXT NOT NULL
);
CREATE TABLE `societies`(
    `society_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` TEXT NOT NULL,
    `description` TEXT NULL,
    `picture` TEXT NOT NULL
);
CREATE TABLE `users`(
    `user_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `name` TINYTEXT NOT NULL,
    `picture` TEXT NOT NULL
);
CREATE TABLE `interests`(
    `interest` VARCHAR(255) NOT NULL,
    `description` TEXT NULL
);
ALTER TABLE
    `interests` ADD PRIMARY KEY(`interest`);
CREATE TABLE `userInterests`(
    `user_id` BIGINT NOT NULL,
    `interest` BIGINT NOT NULL,
    `scale` TINYINT NOT NULL
);
ALTER TABLE
    `userInterests` ADD INDEX `userinterests_user_id_interest_index`(`user_id`, `interest`);

-- Insert randomly generated data into the societies table
INSERT INTO societies (name, description, picture)
SELECT 
    CONCAT('Society ', RAND()),
    CONCAT('Description of Society ', RAND()),
    CONCAT('picture', RAND())
FROM
    information_schema.tables
LIMIT 10;

-- Insert randomly generated data into the users table
INSERT INTO users (username, password, name, picture)
SELECT 
    CONCAT('user', RAND()),
    'password',
    CONCAT('User ', RAND()),
    CONCAT('picture', RAND())
FROM
    information_schema.tables
LIMIT 10;

-- Insert randomly generated data into the events table
INSERT INTO events (society_id, name, description, datetime, location, picture)
SELECT 
    ROUND(RAND() * (SELECT MAX(society_id) FROM societies)),
    CONCAT('Event ', RAND()),
    CONCAT('Description of Event ', RAND()),
    NOW() + INTERVAL ROUND(RAND() * 30) DAY,
    CONCAT('Location ', RAND()),
    CONCAT('picture', RAND())
FROM
    information_schema.tables
LIMIT 10;

-- Insert randomly generated data into the interests table
INSERT INTO interests (interest, description)
SELECT 
    CONCAT('Interest ', RAND()),
    CONCAT('Description of Interest ', RAND())
FROM
    information_schema.tables
LIMIT 10;

-- Insert randomly generated data into the userInterests table
INSERT INTO userInterests (user_id, interest, scale)
SELECT 
    ROUND(RAND() * (SELECT MAX(user_id) FROM users)),
    ROUND(RAND() * (SELECT MAX(interest) FROM interests)),
    ROUND(RAND() * 10)
FROM
    information_schema.tables
LIMIT 10;