CREATE TABLE `societies` (
    `society_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `description` TEXT,
    `image_url` VARCHAR(255),
    UNIQUE (`name`)
);


CREATE TABLE `events` (
    `event_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `event_name` VARCHAR(255) NOT NULL,
    `description` TEXT,
    `location` TEXT,
    `event_time` DATETIME,
    `image_filename` VARCHAR(255),
    `society_id` BIGINT UNSIGNED,
    FOREIGN KEY (`society_id`) REFERENCES `societies`(`id`)
);

CREATE TABLE `users` (
    `user_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `email` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    UNIQUE (`email`)
);

CREATE TABLE `interests` (
    `interest` VARCHAR(255) NOT NULL PRIMARY KEY,
    `description` TEXT NULL
);

CREATE TABLE `userInterests` (
   `user_id` BIGINT UNSIGNED NOT NULL,
   `interest` VARCHAR(255) NOT NULL,
   `scale` TINYINT NOT NULL,
   PRIMARY KEY (`user_id`, `interest`),
   FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`),
   FOREIGN KEY (`interest`) REFERENCES `interests`(`interest`)
);

CREATE TABLE `eventsInterests` (
    `event_id` BIGINT UNSIGNED NOT NULL,
    `interest` VARCHAR(255) NOT NULL,
    `scale` TINYINT NOT NULL,
    PRIMARY KEY (`event_id`, `interest`),
    FOREIGN KEY (`event_id`) REFERENCES `events`(`event_id`),
    FOREIGN KEY (`interest`) REFERENCES `interests`(`interest`)
);

CREATE TABLE `userSocieties` (
    `society_id` BIGINT UNSIGNED NOT NULL,
    `user_id` BIGINT UNSIGNED NOT NULL,
    `join_date` DATE NOT NULL,
    `role` ENUM('commitee', 'member') NOT NULL,
    PRIMARY KEY (`society_id`, `user_id`),
    FOREIGN KEY (`society_id`) REFERENCES `societies`(`society_id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`)
);

CREATE TABLE `userEvents` (
    `user_id` BIGINT UNSIGNED NOT NULL,
    `event_id` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (`user_id`, `event_id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`),
    FOREIGN KEY (`event_id`) REFERENCES `events`(`event_id`)
);

CREATE TABLE `sessions` (
    `user_id` BIGINT UNSIGNED NOT NULL,
    `session_token` VARCHAR(40) NOT NULL,
    PRIMARY KEY (`user_id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`)
);

CREATE TABLE `interestPredictions` (
    `user_id` BIGINT UNSIGNED NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `predicted_interest` DECIMAL(3,2) NOT NULL,
    PRIMARY KEY (`name`, `user_id`),
    FOREIGN KEY (`name`) REFERENCES `societies`(`name`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`)
);

INSERT INTO societies (name, description, image_url) VALUES 
('ABACUS', 'The ABACUS society is for enthusiasts of mathematics and computing.', NULL),
('Badminton', 'Join our Badminton society for friendly matches and tournaments.', NULL),
('Basketball', 'Love basketball? Join our society to play and compete.', NULL),
('Bath City FC soc', 'Supporters of Bath City FC unite in this society to celebrate football.', NULL),
('Boxing', 'Train and spar with fellow members in our Boxing society.', NULL),
('Computer Science soc', 'For students passionate about computer science and programming.', NULL),
('Cricket', 'Join our Cricket society for matches, coaching, and social events.', NULL),
('Cue sports', 'Pool, snooker, and billiards enthusiasts gather here for friendly games.', NULL),
('Cycling', 'Explore the city and countryside on two wheels with our Cycling society.', NULL),
('Dance', 'From salsa to hip-hop, express yourself through dance in our society.', NULL),
('Data science', 'Learn and explore the world of data science with like-minded individuals.', NULL),
('Debate', 'Engage in lively debates and discussions on various topics in our society.', NULL),
('Drum and Bass', 'Fans of Drum and Bass music unite to share their passion.', NULL),
('Fashion', 'Express your style and creativity in our Fashion society.', NULL),
('Finance', 'Learn about finance, investing, and economics in our society.', NULL),
('Fine art', 'Appreciate and create art with fellow artists and enthusiasts.', NULL),
('Gin soc', 'For connoisseurs of gin, join our society for tastings and events.', NULL),
('Golf', 'Tee off and enjoy a round of golf with members of our society.', NULL),
('Green Party', 'Advocate for environmental issues and sustainability with our society.', NULL),
('Hockey', 'Hockey players of all levels are welcome to join our society.', NULL),
('Jiu Jitsu', 'Train in the art of Jiu Jitsu and improve your skills with us.', NULL),
('Lacrosse', 'Join our Lacrosse society for training, matches, and socials.', NULL),
('Left Union', 'A society for those interested in left-wing politics and activism.', NULL),
('Model UN', 'Experience diplomacy and international relations in our Model UN society.', NULL),
('Music soc', 'From classical to rock, celebrate all genres of music with us.', NULL),
('Netball', 'Get active and play netball with our friendly society.', NULL),
('Poker', 'Test your skills and bluffing tactics in our Poker society.', NULL),
('Politics', 'Discuss and debate political issues with members of our society.', NULL),
('Powerlifting', 'Train and compete in powerlifting events with our society.', 'http://localhost:5000/images/powerlifting-society.png'),
('Rowing', 'Rowing enthusiasts gather for training sessions and competitions.', NULL),
('Rugby union', 'Join fellow rugby fans for matches, training, and social events.', NULL),
('Sailing', 'Sail the seas and learn navigation skills with our Sailing society.', NULL),
('Salsa', 'Learn the art of salsa dancing and enjoy Latin rhythms in our society.', NULL),
('Squash', 'Hit the courts and play squash with members of our society.', NULL),
('Student Theatre', 'Get involved in acting, directing, and producing in our Theatre society.', NULL),
('Swimming', 'Dive in and swim laps or relax with our Swimming society.', NULL),
('Table Tennis', 'Play table tennis and compete in tournaments with our society.', NULL),
('Triathlon', 'Train and compete in triathlons with our multi-sport society.', NULL),
('Urban Dance', 'From street to contemporary, express yourself through urban dance.', NULL),
('Water polo', 'Experience the excitement of water polo with our society.', NULL);

INSERT INTO interests (interest, description) VALUES 
('Academic', 'Interest in academic pursuits and intellectual activities'),
('Acting', 'Interest in performing arts and theatrical activities'),
('Americas', 'Interest in the Americas region and its culture'),
('Art', 'Interest in visual arts and creative expression'),
('Asia', 'Interest in the Asian region and its culture'),
('Ball Sport', 'Interest in sports involving a ball, such as football, basketball, etc.'),
('Beginner', 'Interest in beginner-level activities or hobbies'),
('Business', 'Interest in business and entrepreneurial endeavors'),
('Card Games', 'Interest in playing card games and related activities'),
('Clothing', 'Interest in fashion and clothing-related topics'),
('Combat', 'Interest in combat sports and martial arts'),
('Community', 'Interest in community involvement and social activities'),
('Commitment', 'Interest in making commitments and sticking to them'),
('Competitive', 'Interest in competitive activities and challenges'),
('Contact', 'Interest in physical contact sports and activities'),
('Crafts', 'Interest in arts and crafts activities and DIY projects'),
('Creative', 'Interest in creative expression and innovative thinking'),
('Culture', 'Interest in exploring different cultures and traditions'),
('Dance', 'Interest in dancing and rhythmic movement'),
('Data', 'Interest in data analysis and data-related activities'),
('Debating', 'Interest in engaging in debates and discussions'),
('Design', 'Interest in design principles and aesthetic concepts'),
('Discussion', 'Interest in having discussions and exchanging ideas'),
('Entertainment', 'Interest in entertainment and leisure activities'),
('Europe', 'Interest in the European region and its culture'),
('Fantasy', 'Interest in fantasy worlds and imaginative storytelling'),
('Finance', 'Interest in financial matters and investment opportunities'),
('Film & TV', 'Interest in movies, television shows, and cinematic experiences'),
('Fitness', 'Interest in physical fitness and exercise routines'),
('Food & Drink', 'Interest in culinary experiences and beverage choices'),
('Games', 'Interest in playing games and recreational activities'),
('Health', 'Interest in maintaining good health and well-being'),
('History', 'Interest in historical events and past civilizations'),
('Humanities', 'Interest in humanities disciplines and cultural studies'),
('Inclusive', 'Interest in promoting inclusivity and diversity'),
('Individual', 'Interest in individual pursuits and personal development'),
('Indoors', 'Interest in indoor activities and indoor environments'),
('International Politics', 'Interest in global political issues and diplomatic relations'),
('Internal Politics', 'Interest in domestic political matters and government policies'),
('Law', 'Interest in legal principles and justice systems'),
('Literature', 'Interest in literary works and written expression'),
('Mathematics', 'Interest in mathematical concepts and problem-solving'),
('Music', 'Interest in musical compositions and sonic experiences'),
('Outdoors', 'Interest in outdoor activities and nature exploration'),
('Performance', 'Interest in performing in front of an audience'),
('Politics', 'Interest in political ideologies and governance structures'),
('Pub', 'Interest in socializing and gathering at pubs or bars'),
('Public Speaking', 'Interest in public speaking and oratory skills'),
('Racket / Bat Sport', 'Interest in sports involving rackets or bats, such as tennis, badminton, etc.'),
('Reading', 'Interest in reading books and written literature'),
('Relaxing', 'Interest in relaxation techniques and stress relief methods'),
('Religion', 'Interest in religious beliefs and spiritual practices'),
('Roleplay', 'Interest in role-playing games and imaginative scenarios'),
('Running', 'Interest in running and jogging activities'),
('Science', 'Interest in scientific exploration and discovery'),
('Singing', 'Interest in vocal performance and singing'),
('Socialising', 'Interest in social interactions and building relationships'),
('Software', 'Interest in software development and computer programming'),
('Spectating', 'Interest in spectating sports events and live performances'),
('Sport', 'Interest in participating in various sports and physical activities'),
('Strength', 'Interest in building physical strength and muscle mass'),
('Tabletop Games', 'Interest in playing tabletop games and board games'),
('Team', 'Interest in teamwork and collaborative efforts'),
('Technical', 'Interest in technical skills and specialized knowledge'),
('Technology', 'Interest in technological innovations and advancements'),
('Training', 'Interest in training programs and skill development'),
('Travel', 'Interest in traveling to new destinations and exploring different cultures'),
('Videogames', 'Interest in playing video games and interactive digital entertainment'),
('Visual', 'Interest in visual arts and aesthetics'),
('Water Sport', 'Interest in water-based sports and aquatic activities');


INSERT INTO users (email, password) VALUES 
('am4103@bath.ac.uk', 'password'),
('ab1234@test.com', 'password1'),
('a@gmail.com', 'pass'),
('ye1235@test.com', 'password2');


INSERT INTO events (event_name, description, location, event_time, image_filename, society_id) VALUES
('ABACUS Event', 'Description for ABACUS Event', 'Location for ABACUS', '2024-04-15 18:00:00', 'abacus-society.png', 1),
('Badminton Event', 'Description for Badminton Event', 'Location for Badminton', '2024-04-16 19:00:00', 'badminton-society.png', 2),
('Basketball Event', 'Description for Basketball Event', 'Location for Basketball', '2024-04-17 20:00:00', 'basketball-society.png', 3),
('Bath City FC Event', 'Description for Bath City FC Event', 'Location for Bath City FC', '2024-04-18 21:00:00', 'bath-city-fc-society.png', 4),
('Boxing Event', 'Description for Boxing Event', 'Location for Boxing', '2024-04-19 22:00:00', 'boxing-society.png', 5),
('Computer Science Event', 'Description for Computer Science Event', 'Location for Computer Science', '2024-04-20 23:00:00', 'computer-science-society.png', 6),
('Cricket Event', 'Description for Cricket Event', 'Location for Cricket', '2024-04-21 00:00:00', 'cricket-society.png', 7),
('Cue Sports Event', 'Description for Cue Sports Event', 'Location for Cue Sports', '2024-04-22 01:00:00', 'cue-sports-society.png', 8),
('Cycling Event', 'Description for Cycling Event', 'Location for Cycling', '2024-04-23 02:00:00', 'cycling-society.png', 9),
('Dance Event', 'Description for Dance Event', 'Location for Dance', '2024-04-24 03:00:00', 'dance-society.png', 10),
('Data Science Event', 'Description for Data Science Event', 'Location for Data Science', '2024-04-25 04:00:00', 'data-science-society.png', 11),
('Debate Event', 'Description for Debate Event', 'Location for Debate', '2024-04-26 05:00:00', 'debate-society.png', 12),
('Drum and Bass Event', 'Description for Drum and Bass Event', 'Location for Drum and Bass', '2024-04-27 06:00:00', 'drum-and-bass-society.png', 13),
('Fashion Event', 'Description for Fashion Event', 'Location for Fashion', '2024-04-28 07:00:00', 'fashion-society.png', 14),
('Finance Event', 'Description for Finance Event', 'Location for Finance', '2024-04-29 08:00:00', 'finance-society.png', 15),
('Fine Art Event', 'Description for Fine Art Event', 'Location for Fine Art', '2024-04-30 09:00:00', 'fine-art-society.png', 16),
('Gin Event', 'Description for Gin Event', 'Location for Gin', '2024-05-01 10:00:00', 'gin-society.png', 17),
('Golf Event', 'Description for Golf Event', 'Location for Golf', '2024-05-02 11:00:00', 'golf-society.png', 18),
('Green Party Event', 'Description for Green Party Event', 'Location for Green Party', '2024-05-03 12:00:00', 'green-party-society.png', 19),
('Hockey Event', 'Description for Hockey Event', 'Location for Hockey', '2024-05-04 13:00:00', 'http://localhost:5000/images/hockey-society.png', 20),
('Jiu Jitsu Event', 'Description for Jiu Jitsu Event', 'Location for Jiu Jitsu', '2024-05-05 14:00:00', 'jiu-jitsu-society.png', 21),
('Lacrosse Event', 'Description for Lacrosse Event', 'Location for Lacrosse', '2024-05-06 15:00:00', 'lacrosse-society.png', 22),
('Left Union Event', 'Description for Left Union Event', 'Location for Left Union', '2024-05-07 16:00:00', 'left-union-society.png', 23),
('Model UN Event', 'Description for Model UN Event', 'Location for Model UN', '2024-05-08 17:00:00', 'model-un-society.png', 24),
('Music Event', 'Description for Music Event', 'Location for Music', '2024-05-09 18:00:00', 'music-society.png', 25),
('Netball Event', 'Description for Netball Event', 'Location for Netball', '2024-05-10 19:00:00', 'netball-society.png', 26),
('Poker Event', 'Description for Poker Event', 'Location for Poker', '2024-05-11 20:00:00', 'poker-society.png', 27),
('Politics Event', 'Description for Politics Event', 'Location for Politics', '2024-05-12 21:00:00', 'politics-society.png', 28),
('Powerlifting Event', 'Description for Powerlifting Event', 'Location for Powerlifting', '2024-05-13 22:00:00', 'http://localhost:5000/images/powerlifting-society-event-1.png', 29),
('Rowing Event', 'Description for Rowing Event', 'Location for Rowing', '2024-05-14 23:00:00', 'http://localhost:5000/images/rowing-society.png', 30),
('Rugby Union Event', 'Description for Rugby Union Event', 'Location for Rugby Union', '2024-05-15 00:00:00', 'rugby-union-society.png', 31),
('Sailing Event', 'Description for Sailing Event', 'Location for Sailing', '2024-05-16 01:00:00', 'sailing-society.png', 32),
('Salsa Event', 'Description for Salsa Event', 'Location for Salsa', '2024-05-17 02:00:00', 'salsa-society.png', 33),
('Squash Event', 'Description for Squash Event', 'Location for Squash', '2024-05-18 03:00:00', 'squash-society.png', 34),
('Student Theatre Event', 'Description for Student Theatre Event', 'Location for Student Theatre', '2024-05-19 04:00:00', 'student-theatre-society.png', 35),
('Swimming Event', 'Description for Swimming Event', 'Location for Swimming', '2024-05-20 05:00:00', 'swimming-society.png', 36),
('Table Tennis Event', 'Description for Table Tennis Event', 'Location for Table Tennis', '2024-05-21 06:00:00', 'table-tennis-society.png', 37),
('Triathlon Event', 'Description for Triathlon Event', 'Location for Triathlon', '2024-05-22 07:00:00', 'triathlon-society.png', 38),
('Urban Dance Event', 'Description for Urban Dance Event', 'Location for Urban Dance', '2024-05-23 08:00:00', 'urban-dance-society.png', 39),
('Water Polo Event', 'Description for Water Polo Event', 'Location for Water Polo', '2024-05-24 09:00:00', 'water-polo-society.png', 40);

INSERT INTO userInterests (user_id, interest, scale)
SELECT
   users.user_id,
   interests.interest,
   (FLOOR((RAND() * 10))) AS scale             
FROM
   users, interests;

INSERT INTO userSocieties (society_id, user_id, join_date, role) VALUES
('1', '1', CURRENT_DATE, 'member'),
('1', '2', CURRENT_DATE, 'commitee');

INSERT INTO interestPredictions (name, user_id, predicted_interest)
SELECT
   societies.name,
   users.user_id,
   0 AS predicted_interest             
FROM
   societies, users;


/*             select all users in a society, or every society a user is in
SELECT users.name, societies.name AS society, userSocieties.role 
FROM userSocieties 
INNER JOIN users ON users.user_id = userSocieties.user_id 
INNER JOIN societies ON userSocieties.society_id = societies.society_id 
WHERE userSocieties.society_id = 1;
*/

/*               select 10 highest interests for a given user 
SELECT *
FROM userInterests
WHERE user_id = 1
ORDER BY scale DESC
LIMIT 10;
*/
