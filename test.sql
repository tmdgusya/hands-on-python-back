CREATE TABLE user_account (
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(30),
    fullname VARCHAR(255),
    PRIMARY KEY (id)
);

CREATE TABLE address (
    id INT AUTO_INCREMENT NOT NULL,
    email_address VARCHAR(255) NOT NULL,
    user_id INT NOT NULL,
    PRIMARY KEY (id)
);