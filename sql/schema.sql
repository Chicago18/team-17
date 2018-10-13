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

CREATE TABLE resources(
  name VARCHAR(10) NOT NULL,
  body VARCHAR(200) NOT NULL,
  person VARCHAR(20) NOT NULL,
  PRIMARY KEY (name)
);

CREATE TABLE discussion(
  post VARCHAR(20) NOT NULL,
  body VARCHAR(100) NOT NULL,
  person VARCHAR(20) NOT NULL,
  PRIMARY KEY (post)
);

CREATE TABLE testimony(
  name VARCHAR(20) NOT NULL,
  title VARCHAR(100) NOT NULL,
  location VARCHAR(20) NOT NULL,
  affiliation VARCHAR(20) NOT NULL,
  company VARCHAR(20) NOT NULL,
  email VARCHAR(20) NOT NULL,
  PRIMARY KEY (name)
);