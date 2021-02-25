
USE elearning;


CREATE TABLE IF NOT EXISTS categories (
            ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            category VARCHAR (200) NOT NULL,
            UNIQUE (category)
            );

CREATE TABLE IF NOT EXISTS videos (
            ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            link VARCHAR(200),
            title VARCHAR(200) NOT NULL,
            author VARCHAR(200) NOT NULL,
            categoryid INT NOT NULL,
            duration VARCHAR(200) NOT NULL,
            ranking INT NOT NULL,
            FOREIGN KEY (categoryID) REFERENCES categories(ID),
            UNIQUE (link)
            );
            
CREATE TABLE IF NOT EXISTS users (
            ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(200) NOT NULL,
            email VARCHAR(200) NOT NULL,
            passeword VARCHAR(200) NOT NULL,
            UNIQUE (pseudo, email)
            );



INSERT INTO categories (category) VALUES
                        ('Python'),
                        ('Javascript'),
                        ('HTML'),
                        ('CSS'),
                        ('Docker'),
                        ('Bash'),
                        ('Cloud'),
                        ('Cryptographie');

INSERT INTO videos (link, title, author, categoryid, duration, ranking) VALUES
    ('https://www.youtube.com/watch?v=psaDHhZ0cPs', 'APPRENDRE LE PYTHON #1 ? LES BASES & PREREQUIS', 'Graven - Développement', 1, '00:09:27', 4.93),
    ('https://www.youtube.com/watch?v=9Os0o3wzS_I', 'Python Tutorial for Beginners 8: Functions', 'Corey Schafer', 1, '00:21:47', 4.94),
    ('https://www.youtube.com/watch?v=apACNr7DC_s&t=117s', 'Python Classes and Objects  ||  Python Tutorial  ||  Learn Python Programming', 'Socratica', 1, '00:10:32', 4.92),
    ('https://www.youtube.com/watch?v=NmM9HA2MQGI', 'Secret Key Exchange (Diffie-Hellman) - Computerphile', 'Computerphile', 8, '00:08:40', 4.94),
    ('https://www.youtube.com/watch?v=KOdfpbnWLVo', 'Hello World in Python ||  Python Tutorial  ||  Python Programming', 'Socratica', 1, '00:02:47', 4.9),
    ('https://www.youtube.com/watch?v=lsMQRaeKNDk', 'What is a REST API?', 'IBM Cloud', 7, '00:09:12', 4.89),
    ('https://www.youtube.com/watch?v=QJ4fODH6DXI', 'Kubernetes Concepts Explained in 9 minutes!', 'KodeKloud', 5, '00:09:50', 4.94),
    ('https://www.youtube.com/watch?v=Pt9LelJ0fL0', 'AZ-900 Episode 1 | Cloud Computing and Vocabulary | Microsoft Azure Fundamentals Full Course', 'Adam Marczak - Azure for Everyone', 5, '00:09:40', 4.99),
    ('https://www.youtube.com/watch?v=vsXMMT2CqqE', 'Key Exchange Problems - Computerphile', 'Computerphile', 8, '00:09:17', 4.98),
    ('https://www.youtube.com/watch?v=cqgtdkURzTE', 'Cryptography For Beginners', 'Coding Tech', 8, '00:45:17', 4.91),
    ('https://www.youtube.com/watch?v=XF1_MlZ5l6M&ab_channel=WebDevSimplified', 'Learn JavaScript Event Listeners In 18 Minutes', 'Web Dev Simplified', 2, '00:18:03', 4.98),
    ('https://www.youtube.com/watch?v=h33Srr5J9nY&ab_channel=WebDevSimplified', 'JavaScript ES6 Arrow Functions Tutorial', 'Web Dev Simplified', 2, '00:09:32', 4.95),
    ('https://www.youtube.com/watch?v=DHvZLI7Db8E&ab_channel=WebDevSimplified', 'JavaScript Promises In 10 Minutes', 'Web Dev Simplified', 2, '00:11:31', 4.94);



