CREATE TABLE users(
  username VARCHAR(20) NOT NULL,
  fullname VARCHAR(40) NOT NULL,
  location VARCHAR(20) NOT NULL,
  email VARCHAR(40) NOT NULL,
  company VARCHAR(20) NOT NULL,
  affiliation VARCHAR(20) NOT NULL,
  password VARCHAR(256) NOT NULL,
  created DATETIME default current_timestamp NOT NULL,
  PRIMARY KEY (username)
);