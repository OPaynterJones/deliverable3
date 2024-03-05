CREATE TABLE `events` (
    `event_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `society_id` BIGINT UNSIGNED NOT NULL,
    `name` TINYTEXT NOT NULL,
    `description` TEXT NULL,
    `datetime` DATETIME NOT NULL,
    `location` TINYTEXT NOT NULL,
    `picture` TINYTEXT NULL
);

CREATE TABLE `societies` (
    `society_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL,
    `description` TEXT NULL,
    `picture` TEXT NULL,
    UNIQUE (`name`)
);

CREATE TABLE `users` (
    `user_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `email` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    UNIQUE (`email`)
);

CREATE TABLE `interests` (
    `interest` VARCHAR(255) NOT NULL PRIMARY KEY,
    `description` TEXT NULL,
    `category` ENUM('Sport', 'Games', 'Socializing', 'Academic', 'Creative') NOT NULL
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

-- Insert list of societies and some generic description
INSERT INTO societies (name, description, picture) VALUES 
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
('Powerlifting', 'Train and compete in powerlifting events with our society.', NULL),
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

-- Insert list of interests and some generic description
INSERT INTO interests (interest, description, category) VALUES 
('Contact Sports', 'Engage in physical activities involving direct contact with opponents.', 'Sport'),
('Tabletop', 'Enjoy board games, card games, and other tabletop gaming activities.', 'Games'),
('Pub', 'Socialize and relax in pub environments, often involving drinks and conversation.', 'Socializing'),
('Humanities', 'Explore various aspects of human culture, such as history, philosophy, and literature.', 'Academic'),
('Dance', 'Express yourself through rhythmic movement and choreography.', 'Creative'),
('Combat Sport', 'Participate in sports involving physical combat or self-defense techniques.', 'Sport'),
('Cards', 'Play card games and enjoy strategic thinking and luck-based gameplay.', 'Games'),
('Outdoor', 'Enjoy activities and events that take place in outdoor environments.', 'Socializing'),
('Religion', 'Discuss and study beliefs, rituals, and spiritual practices of different religions.', 'Academic'),
('Singing', 'Express yourself through vocal performance and harmonization.', 'Creative'),
('Running', 'Engage in the physical activity of running, either competitively or recreationally.', 'Sport'),
('Videogames', 'Play electronic games involving interaction with a user interface to generate visual feedback.', 'Games'),
('Indoor Sports', 'Participate in activities and events that take place indoors.', 'Sport'),
('Literature', 'Explore written works, including novels, poetry, and essays.', 'Academic'),
('Acting', 'Portray characters and perform dramatic roles in theatrical productions.', 'Creative'),
('Water Sport', 'Participate in sports and recreational activities that take place in or on water.', 'Sport'),
('Fantasy', 'Explore imaginative settings and elements often found in literature and entertainment.', 'Games'),
('Performance', 'Engage in activities involving public presentation or entertainment.', 'Creative'),
('Politics', 'Discuss and engage in activities related to governance, political systems, and policies.', 'Academic'),
('Culture', 'Explore and celebrate the customs, traditions, and arts of different societies.', 'Creative'),
('Racket Sport', 'Engage in sports involving the use of rackets or paddles, such as tennis or badminton.', 'Sport'),
('Role Play', 'Take on fictional roles and engage in collaborative storytelling.', 'Games'),
('International Politics', 'Discuss and analyze interactions between nations and global affairs.', 'Academic'),
('Law', 'Study legal systems, principles, and practices.', 'Academic'),
('Public Speaking', 'Develop and practice the skill of delivering speeches and presentations to an audience.', 'Creative'),
('Ball Sport', 'Participate in sports involving the use of balls, such as soccer, basketball, or volleyball.', 'Sport'),
('Individual', 'Engage in activities that focus on personal development and solitary pursuits.', 'Socializing'),
('Internal Politics', 'Discuss and engage in activities related to organizational or group governance and dynamics.', 'Academic'),
('History', 'Study past events, societies, and civilizations.', 'Academic'),
('Fitness', 'Participate in activities aimed at improving physical health and conditioning.', 'Sport'),
('Technical', 'Engage in activities involving specialized knowledge or skills, often related to technology or machinery.', 'Socializing'),
('Finance', 'Study and manage monetary resources, investments, and financial systems.', 'Academic'),
('Crafts', 'Create handmade objects or artworks through skilled craftsmanship.', 'Creative'),
('Health', 'Focus on activities and practices aimed at promoting physical and mental well-being.', 'Sport'),
('Inclusive', 'Promote and participate in activities that welcome and accommodate diverse participants.', 'Socializing'),
('Business', 'Explore and engage in activities related to commerce, trade, and entrepreneurship.', 'Academic'),
('Design', 'Create and innovate in fields such as graphic design, industrial design, or architecture.', 'Creative'),
('Strength', 'Focus on activities aimed at developing physical strength and power.', 'Sport'),
('Community', 'Engage with and contribute to local or online communities.', 'Socializing'),
('Science', 'Explore the natural world through observation, experimentation, and analysis.', 'Academic'),
('Spectating', 'Enjoy watching and observing sports, performances, or other events.', 'Creative'),
('Travel', 'Explore new destinations and cultures through travel and adventure.', 'Socializing'),
('Technology', 'Explore and engage with advancements in science and engineering.', 'Academic'),
('Music', 'Appreciate, perform, or create music across various genres and styles.', 'Creative'),
('Asia', 'Explore the cultures, history, and geography of Asian countries and regions.', 'Socializing'),
('Software', 'Engage with and develop software applications and computer programs.', 'Academic'),
('Film & TV', 'Enjoy and analyze movies, television shows, and cinematic storytelling.', 'Creative'),
('Europe', 'Explore the cultures, history, and geography of European countries and regions.', 'Socializing'),
('Data', 'Analyze and interpret data to derive insights and make informed decisions.', 'Academic'),
('Clothing', 'Explore fashion trends, styles, and clothing design.', 'Creative'),
('Americas', 'Explore the cultures, history, and geography of the Americas.', 'Socializing'),
('Mathematics', 'Explore mathematical concepts, theories, and applications.', 'Academic'),
('Visual', 'Engage with and create visual artworks, including drawing, painting, and photography.', 'Creative'),
('Discussion', 'Engage in conversations and debates on various topics and issues.', 'Socializing'),
('Commitment', 'Participate in activities or organizations with a dedicated and loyal mindset.', 'Socializing'),
('Relaxing', 'Engage in activities aimed at reducing stress and promoting relaxation.', 'Socializing'); 

INSERT INTO users (email, password) VALUES 
('am4103@bath.ac.uk', 'password'),
('ab1234@test.com', 'password1'),
('ye1235@test.com', 'password2');

INSERT INTO userInterests (user_id, interest, scale)
SELECT
    users.user_id,
    interests.interest,
    64 AS scale             
FROM
    users, interests;

INSERT INTO userSocieties (society_id, user_id, join_date, role) VALUES
('1', '1', CURRENT_DATE, 'member'),
('1', '2', CURRENT_DATE, 'commitee');

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
