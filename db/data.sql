

CREATE database IF NOT EXISTS elearning;
USE elearning;



CREATE TABLE IF NOT EXISTS categories (
            ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            category VARCHAR (200)
            );

CREATE TABLE IF NOT EXISTS video (
            link VARCHAR(200) PRIMARY KEY,
            title VARCHAR(200) NOT NULL,
            author VARCHAR(200) NOT NULL,
            duration VARCHAR(200) NOT NULL,
            category VARCHAR(200) NOT NULL,
            ranking INT NOT NULL
            );
            
CREATE TABLE IF NOT EXISTS users (\
            ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            mail VARCHAR(200) NOT NULL,
            pwd VARCHAR(200) NOT NULL
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

INSERT INTO video (link, title, author, duration, category, ranking) VALUES
    ('https://www.youtube.com/watch?v=NmM9HA2MQGI', 'Secret Key Exchange (Diffie-Hellman) - Computerphile', 'Computerphile', 'Cryptographie', '00:08:40', 4.94),
    ('https://www.youtube.com/watch?v=KOdfpbnWLVo', 'Hello World in Python ||  Python Tutorial  ||  Python Programming', 'Socratica', 'Python', '00:02:47', 4.9),
    ('https://www.youtube.com/watch?v=lsMQRaeKNDk', 'What is a REST API?', 'IBM Cloud', 'Cloud', '00:09:12', 4.89),
    ('https://www.youtube.com/watch?v=QJ4fODH6DXI', 'Kubernetes Concepts Explained in 9 minutes!', 'KodeKloud', 'Docker', '00:09:50', 4.94),
    ('https://www.youtube.com/watch?v=Pt9LelJ0fL0', 'AZ-900 Episode 1 | Cloud Computing and Vocabulary | Microsoft Azure Fundamentals Full Course', 'Adam Marczak - Azure for Everyone', 'Cloud', '00:09:40', 4.99),
    ('https://www.youtube.com/watch?v=vsXMMT2CqqE', 'Key Exchange Problems - Computerphile', 'Computerphile', 'Cryptographie', '00:09:17', 4.98),
    ('https://www.youtube.com/watch?v=cqgtdkURzTE', 'Cryptography For Beginners', 'Coding Tech', 'Cryptographie', '00:45:17', 4.91),
    ('https://www.youtube.com/watch?v=XF1_MlZ5l6M&ab_channel=WebDevSimplified', 'Learn JavaScript Event Listeners In 18 Minutes', 'Web Dev Simplified', 'Javascript', '00:18:03', 4.98),
    ('https://www.youtube.com/watch?v=h33Srr5J9nY&ab_channel=WebDevSimplified', 'JavaScript ES6 Arrow Functions Tutorial', 'Web Dev Simplified', 'Javascript', '00:09:32', 4.95),
    ('https://www.youtube.com/watch?v=DHvZLI7Db8E&ab_channel=WebDevSimplified', 'JavaScript Promises In 10 Minutes', 'Web Dev Simplified', 'Javascript', '00:11:31', 4.94);



