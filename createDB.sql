#create database
CREATE DATABASE SurveysDB;

#select database
USE SurveysDB;

#create survey table
CREATE TABLE Survey (
	survey_id INT(4) ZEROFILL AUTO_INCREMENT PRIMARY KEY,
	fullname VARCHAR(100) NOT NULL,
	email VARCHAR(100) NOT NULL,
	age INT NOT NULL,
	contact_number VARCHAR(20) NOT NULL,
	pizza INT NOT NULL,
	pasta INT NOT NULL,
	pap_and_wors INT NOT NULL,
	other INT NOT NULL,
	movies INT NOT NULL,
	radio INT NOT NULL,
	eat_out INT NOT NULL,
	tv INT NOT NULL
);

#display table to confirm creation
SHOW TABLES;