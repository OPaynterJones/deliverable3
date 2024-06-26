CREATE TABLE `societies` (
    `society_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `description` TEXT,
    `requirements` TEXT,
    `location` TEXT,
    `meeting_time` TEXT,
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
    FOREIGN KEY (`society_id`) REFERENCES `societies`(`society_id`)
);



CREATE TABLE `users` (
    `user_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `email` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    UNIQUE (`email`)
);


CREATE TABLE `servedEvents` (
    `user_id` BIGINT UNSIGNED NOT NULL,
    `event_id` BIGINT UNSIGNED NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`),
    FOREIGN KEY (`event_id`) REFERENCES `events`(`event_id`)
);

CREATE TABLE `interests` (
    `interest` VARCHAR(255) NOT NULL PRIMARY KEY,
    `description` TEXT NULL
);

CREATE TABLE `userInterests` (
   `user_id` BIGINT UNSIGNED NOT NULL,
   `interest` VARCHAR(255) NOT NULL,
   `scale` TINYINT NOT NULL DEFAULT 3,
   PRIMARY KEY (`user_id`, `interest`),
   FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`),
   FOREIGN KEY (`interest`) REFERENCES `interests`(`interest`)
);

-- CREATE TABLE `eventsInterests` (
--     `event_id` BIGINT UNSIGNED NOT NULL,
--     `interest` VARCHAR(255) NOT NULL,
--     `scale` TINYINT NOT NULL,
--     PRIMARY KEY (`event_id`, `interest`),
--     FOREIGN KEY (`event_id`) REFERENCES `events`(`event_id`),
--     FOREIGN KEY (`interest`) REFERENCES `interests`(`interest`)
-- );

CREATE TABLE `userSocieties` (
    `society_id` BIGINT UNSIGNED NOT NULL,
    `user_id` BIGINT UNSIGNED NOT NULL,
    `role` ENUM('commitee', 'member') NOT NULL,
    PRIMARY KEY (`society_id`, `user_id`),
    FOREIGN KEY (`society_id`) REFERENCES `societies`(`society_id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`)
);

-- CREATE TABLE `userEvents` (
--     `user_id` BIGINT UNSIGNED NOT NULL,
--     `event_id` BIGINT UNSIGNED NOT NULL,
--     PRIMARY KEY (`user_id`, `event_id`),
--     FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`),
--     FOREIGN KEY (`event_id`) REFERENCES `events`(`event_id`)
-- );

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

INSERT INTO societies (name, description, requirements, location, meeting_time, image_url) VALUES 
('Hockey', 'HOckey description', 'hockey experience', 'hockey lockation', 'hockey time', '/images/hockey-society.png'),
('Powerlifting', 'Train and compete in powerlifting events with our society.', 'no previous experience needed. Equiptment is commonly used, but is by no means a barrier to entry. All forms of fitness welcome!', 'Jumps and throws hall, sports training village', 'Every monday 2000-2200', '/images/powerlifting-society.png'),
('Rowing', 'Rowing description', 'Rowing experience', 'Rowing lockation', 'Rowing time', '/images/rowing-society.png'),
('ABACUS', 'The ABACUS society is for enthusiasts of mathematics and computing.', 'Mathematics and computing enthusiasts', 'Mathematics building, Room 101', 'Every Thursday 18:00-20:00', NULL),
('Badminton', 'Join our Badminton society for friendly matches and tournaments.', 'Beginners welcome', 'Sports hall', 'Every Tuesday and Friday 17:00-19:00', NULL),
('Basketball', 'Love basketball? Join our society to play and compete.', 'All skill levels', 'Basketball court, Sports Complex', 'Every Wednesday 19:00-21:00', NULL),
('Bath City FC soc', 'Supporters of Bath City FC unite in this society to celebrate football.', 'Football supporters', 'Bath City FC Stadium', 'Matchdays', NULL),
('Boxing', 'Train and spar with fellow members in our Boxing society.', 'All skill levels', 'Boxing gym, Sports Complex', 'Every Monday and Thursday 18:00-20:00', NULL),
('Computer Science soc', 'For students passionate about computer science and programming.', 'Computer science enthusiasts', 'Computer science building, Room 202', 'Every Friday 16:00-18:00', NULL),
('Cricket', 'Join our Cricket society for matches, coaching, and social events.', 'Beginners welcome', 'Cricket field', 'Every Sunday 10:00-13:00', NULL),
('Cue sports', 'Pool, snooker, and billiards enthusiasts gather here for friendly games.', 'Cue sports enthusiasts', 'Cue sports room, Student Union', 'Every Thursday 19:00-21:00', NULL),
('Cycling', 'Explore the city and countryside on two wheels with our Cycling society.', 'All skill levels', 'Cycle track', 'Every Saturday 09:00-12:00', NULL),
('Dance', 'From salsa to hip-hop, express yourself through dance in our society.', 'All dance styles', 'Dance studio, Arts building', 'Every Wednesday 17:00-19:00', NULL),
('Data science', 'Learn and explore the world of data science with like-minded individuals.', 'Data science enthusiasts', 'Data science lab, Computer science building', 'Every Tuesday 18:00-20:00', NULL),
('Debate', 'Engage in lively debates and discussions on various topics in our society.', 'Debate enthusiasts', 'Debate room, Student Union', 'Every Thursday 16:00-18:00', NULL),
('Drum and Bass', 'Fans of Drum and Bass music unite to share their passion.', 'Drum and Bass music fans', 'Music room, Student Union', 'Every Friday 20:00-22:00', NULL),
('Fashion', 'Express your style and creativity in our Fashion society.', 'Fashion enthusiasts', 'Fashion studio, Arts building', 'Every Monday 14:00-16:00', NULL),
('Finance', 'Learn about finance, investing, and economics in our society.', 'Finance enthusiasts', 'Finance lab, Business school', 'Every Wednesday 18:00-20:00', NULL),
('Fine art', 'Appreciate and create art with fellow artists and enthusiasts.', 'Art enthusiasts', 'Art studio, Arts building', 'Every Saturday 14:00-16:00', NULL),
('Gin soc', 'For connoisseurs of gin, join our society for tastings and events.', 'Gin enthusiasts', 'Gin tasting room, Student Union', 'Monthly, dates vary', NULL),
('Golf', 'Tee off and enjoy a round of golf with members of our society.', 'All skill levels', 'Golf course', 'Every Sunday 09:00-12:00', NULL),
('Green Party', 'Advocate for environmental issues and sustainability with our society.', 'Environmental activists', 'Environmental science building, Room 303', 'Monthly meetings', NULL),
('Jiu Jitsu', 'Train in the art of Jiu Jitsu and improve your skills with us.', 'All skill levels', 'Jiu Jitsu dojo, Sports Complex', 'Every Monday and Thursday 20:00-22:00', NULL),
('Lacrosse', 'Join our Lacrosse society for training, matches, and socials.', 'All skill levels', 'Lacrosse field', 'Every Tuesday and Thursday 17:00-19:00', NULL),
('Left Union', 'A society for those interested in left-wing politics and activism.', 'Left-wing politics enthusiasts', 'Political science building, Room 105', 'Monthly meetings', NULL),
('Model UN', 'Experience diplomacy and international relations in our Model UN society.', 'Model UN enthusiasts', 'Model UN room, Student Union', 'Every Friday 18:00-20:00', NULL),
('Music soc', 'From classical to rock, celebrate all genres of music with us.', 'Music enthusiasts', 'Music room, Student Union', 'Every Wednesday 20:00-22:00', NULL),
('Netball', 'Get active and play netball with our friendly society.', 'All skill levels', 'Netball court, Sports Complex', 'Every Monday and Wednesday 18:00-20:00', NULL),
('Poker', 'Test your skills and bluffing tactics in our Poker society.', 'Poker enthusiasts', 'Poker room, Student Union', 'Every Thursday 20:00-22:00', NULL),
('Politics', 'Discuss and debate political issues with members of our society.', 'Politics enthusiasts', 'Politics room, Student Union', 'Every Tuesday 17:00-19:00', NULL),
('Rugby union', 'Join fellow rugby fans for matches, training, and social events.', 'Rugby fans', 'Rugby field', 'Matchdays', NULL),
('Sailing', 'Sail the seas and learn navigation skills with our Sailing society.', 'All skill levels', 'Sailing club, Marina', 'Every Sunday 10:00-12:00', NULL),
('Salsa', 'Learn the art of salsa dancing and enjoy Latin rhythms in our society.', 'All dance levels', 'Dance studio, Arts building', 'Every Thursday 19:00-21:00', NULL),
('Squash', 'Hit the courts and play squash with members of our society.', 'All skill levels', 'Squash court, Sports Complex', 'Every Monday and Friday 19:00-21:00', NULL),
('Student Theatre', 'Get involved in acting, directing, and producing in our Theatre society.', 'Theatre enthusiasts', 'Theatre auditorium, Arts building', 'Every Saturday 16:00-18:00', NULL),
('Swimming', 'Dive in and swim laps or relax with our Swimming society.', 'All skill levels', 'Swimming pool, Sports Complex', 'Every Tuesday and Thursday 19:00-21:00', NULL),
('Table Tennis', 'Play table tennis and compete in tournaments with our society.', 'All skill levels', 'Table tennis hall, Sports Complex', 'Every Wednesday and Friday 18:00-20:00', NULL),
('Triathlon', 'Train and compete in triathlons with our multi-sport society.', 'All skill levels', 'Triathlon track, Sports Complex', 'Every Sunday 07:00-10:00', NULL),
('Urban Dance', 'From street to contemporary, express yourself through urban dance.', 'All dance styles', 'Dance studio, Arts building', 'Every Friday 17:00-19:00', NULL),
('Water polo', 'Experience the excitement of water polo with our society.', 'All skill levels', 'Water polo pool, Sports Complex', 'Every Tuesday and Thursday 18:00-20:00', NULL);

INSERT INTO events (event_name, description, location, event_time, image_filename, society_id) VALUES
('Hockey Event', 'Description for Hockey Event', 'Location for Hockey', '2024-05-04 13:00:00', '/images/hockey-society.png', 1),
('Powerlifting Event', 'Description for Powerlifting Event', 'Location for Powerlifting', '2024-05-13 22:00:00', '/images/powerlifting-society-event-1.png', 2),
('Rowing Event', 'Description for Rowing Event', 'Location for Rowing', '2024-05-24 09:00:00', '/images/rowing-society.png', 3),
('Badminton Taster Session', 'Come down and give badminton a try, all skill levels welcome', 'STV hall 1 (courts 1-4)', '2024-05-12 13:00:00','/images/badminton.jpeg', 5),
('Boxing Fight Night', 'We have a packed night of 8 fights, make sure to get your tickets in advance to ensure your place!', 'Komedia', '2024-05-14 19:00:00', '/images/boxing.jpeg', 8),
('Computer Science pub quiz night', 'Come and join us for this casual pub night, entries are £5 per team', 'The West Gate', '2024-05-12 20:00:00', '/images/compsci.jpeg', 9),
('Cue sports Pool Tournament','Test your skills in our cue sports tournament! Compete against fellow enthusiasts for bragging rights and prizes.', 'SU Pool area', '2024-05-20 18:00:00', '/images/pool.jpeg', 11),
('Cycling Charity Ride', 'Pedal for a cause with our cycling charity ride. Enjoy scenic routes while raising funds for a worthy charity.', 'Starting Point: Outside the STV main entrance', '2024-05-22 10:00:00','/images/cycling.jpeg', 12),
('Data Science Symposium', 'Delve into the world of data science with expert speakers and engaging discussions. Open to all curious minds!', 'Tech Hub Auditorium', '2024-05-28 16:00:00','/images/datascience.jpeg', 14),
('Dance Showcase', 'Experience an electrifying evening of dance performances showcasing a variety of styles and talents. Don''t miss out!', 'The Dance Studio, the Edge', '2024-05-25 19:00:00','/images/dance.jpeg', 13),
('Debate society: Animal testing','Sharpen your argumentative skills and engage in intellectual sparring at our debate meeting. May the most persuasive prevail!', 'Chancellors building 3.06', '2024-05-30 18:00:00', '/images/debate.jpeg', 15),
('Drum and Bass DJ Night', 'Get ready to dance the night away to the beats of drum and bass with top DJs spinning the latest tracks.', 'The Tub (SU)', '2024-06-02 20:00:00', '/images/drumandbase.jpeg', 16),
('Fashion Show Extravaganza', 'Witness the latest trends and designs strut down the runway in our glamorous fashion show extravaganza. A night of style awaits!', 'The Edge Studio 1', '2024-06-05 19:00:00', '/images/fashion.jpeg', 17),
('Finance Workshop Series', 'Gain valuable insights into the world of finance with our comprehensive workshop series led by industry experts.', 'Chancellors Building 1.10', '2024-06-08 13:00:00', '/images/finance.jpeg', 18),
('Fine Art Exhibition Opening', 'Immerse yourself in a world of creativity and beauty at the opening of our fine art exhibition, featuring works by talented local artists.', 'Claverton Rooms', '2024-06-10 15:00:00', '/images/fineart.jpeg', 19),
('Gin pub crawl', 'We''ll be doing a crawl of all the best pubs in Bath (drinking alcohol not required)', 'Start Point: The Cork', '2024-05-12 20:00:00','/images/gin.jpeg', 20),
('Golf Tournament', 'Tee off for a day of friendly competition and camaraderie at our golf tournament. Prizes await the top performers!', 'Bath Golf Clubhouse', '2024-05-15 14:00:00', '/images/golf.jpeg', 21),
('Green Party Rally', 'Join us in advocating for environmental sustainability and social justice at our Green Party rally. Together, we can make a difference!', 'City Park Amphitheater', '2024-06-18 13:00:00', '/images/greenparty.jpeg', 22),
('Hockey Trails', 'Come down and see if you have the skills to make it into one of our BUCS teams!', 'Hockey Astro 1, STV', '2024-05-17 12:00:00', '/images/hockey.jpeg', 1),
('Jiu Jitsu Workshop', 'Learn essential techniques and hone your skills in the ancient art of Jiu Jitsu at our hands-on workshop. Beginners welcome!', 'Martial Arts Dojo, STV', '2024-05-22 11:00:00', '/images/jiujitsu.jpeg', 23),
('Lacrosse Skills Clinic', 'Improve your lacrosse skills and techniques with personalized instruction from experienced coaches at our skills clinic.', 'Lacrosse Field', '2024-05-25 14:00:00', '/images/lacrosse.jpeg', 24),
('Left Union Forum', 'Join us for stimulating discussions on progressive politics and social change at the Left Union forum. Your voice matters!', 'Chancellors building 4.02', '2024-05-28 13:00:00', '/images/leftunion.jpeg', 25),
('Model UN Conference', 'Step into the shoes of diplomats and negotiate global issues at our Model UN conference. Diplomacy and debate await!', 'East Building 0.11', '2024-04-30 18:00:00', '/images/modelun.jpeg', 26),
('Music Society - Band Night', 'Be captivated by the melodious performances of our talented musicians and bands at the Student Union.', 'The Plug (SU)', '2024-05-02 19:00:00', '/images/music.jpeg', 27),
('Netball Tournament', 'Shoot, pass, and score your way to victory in our exciting netball tournament. Gather your team and join the competition!', 'Netball Courts 1-4', '2024-05-05 14:00:00', '/images/netball.jpeg', 28),
('Poker Night Showdown', 'Ante up and test your poker face in our high-stakes poker night showdown.', '1 West 1.11', '2024-07-08 19:00:00', '/images/poker.jpeg', 29),
('Political Debate Series', 'Engage in lively debates on pressing political issues at our debate series. A platform for diverse perspectives and constructive dialogue.', '10 West 0.11', '2024-05-10 19:00:00', '/images/politics.jpeg', 30),
('Powerlifting Competition', 'Witness feats of strength and determination at our powerlifting competition. Lifters of all levels welcome to compete!', 'Gym 1', '2024-05-12 13:00:00', '/images/powerlifting.jpeg', 2),
('Rowing - BUCS Regatta', 'One of the biggest and best racing events of the year. From GB trialists to novices we''ll be competing in all levels of sculling and sweeping!', 'holme pierrepont country park, Nottingham', '2024-05-15 09:00:00', '/images/rowing.jpg', 3),
('BUCS Rugby Union vs UWE', 'Experience the intensity and excitement of rugby as we clash against UWE.', 'STV Rugby Pitch (athletcis track)', '2024-05-18 17:00:00','/images/rugby.jpeg', 31),
('Sailing Adventure Day', 'Set sail for adventure with our sailing day trip. Whether you''re a novice or seasoned sailor, there''s fun to be had on the open sea!', 'Marina Dock, Southampton', '2024-05-20 08:00:00', '/images/sailing.jpeg', 32),
('Salsa Dance Party', 'Move to the rhythm of salsa music and heat up the dance floor at our salsa dance party. No partner required, just your dancing shoes!', 'The Edge Studio 1', '2024-05-22 15:00:00', '/images/salsa.jpeg', 33),
('Squash Tournament', 'Squash your opponents and claim victory in our fast-paced squash tournament. Test your agility and reflexes on the court!', 'Squash Courts', '2024-05-25 13:00:00', '/images/squash.jpeg', 34),
('Student Theatre Production - Beauty and the Beast', 'Be entertained by the creativity and talent of our student performers in an unforgettable theatre production of Beauty and the Beast. Tickets can be bought online or on the door (if available)', 'The Edge Theater', '2024-05-28','/images/theatre.jpeg', 35),
('Swimming Gala', 'Dive into the excitement of our swimming gala, where competitors race for glory in various swimming events', 'Olympic Pool Complex', '2024-05-30', '/images/swimming.jpeg', 36),
('Table Tennis Championship', 'Serve, spin, and smash your way to victory in our table tennis championship. Show off your skills and claim the title!', 'Founders Hall', '2024-05-02', '/images/tabletennis.jpeg', 37),
('Triathlon Challenge', 'Push your limits and test your endurance in our triathlon challenge. Swim, bike, and run your way to the finish line!', 'Starting Line: Bournmouth Beachfront', '2024-05-05', '/images/triathlon.jpeg', 38),
('Urban Dance Workshop', 'Groove to the latest beats and learn urban dance moves from talented instructors at our dynamic workshop.', 'The Edge Studio 2', '2024-05-08', '/images/urbandance.jpeg', 39),
('Water Polo Match vs Cardiff Met', 'Come and support the teams we take on both the mens and womens teams from Cardiff Met!', 'Olympic Swimming Pool, STV', '2024-05-10', '/images/waterpolo.jpeg', 40);




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

INSERT INTO userInterests (user_id, interest, scale)
SELECT
   users.user_id,
   interests.interest,
   (FLOOR((RAND() * 10))) AS scale             
FROM
   users, interests;

INSERT INTO interestPredictions (name, user_id, predicted_interest)
SELECT
   societies.name,
   users.user_id,
   0 AS predicted_interest             
FROM
   societies, users;