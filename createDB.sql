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
	pizza BOOLEAN NOT NULL,
	pasta BOOLEAN NOT NULL,
	pap_and_wors BOOLEAN NOT NULL,
	other BOOLEAN NOT NULL,
	movies TYNYINT NOT NULL,
	radio TYNYINT NOT NULL,
	eat_out TYNYINT NOT NULL,
	tv TYNYINT NOT NULL
);

#display table to confirm creation
SHOW TABLES;