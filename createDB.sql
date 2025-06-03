-- Create database
CREATE DATABASE surveysdb;

-- Connect to the database (use `\c surveysdb` if using psql CLI)
-- or switch databases via your tool (e.g., pgAdmin)

-- Create survey table
CREATE TABLE survey (
    survey_id SERIAL PRIMARY KEY,
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

-- Show tables (in psql CLI)
-- \dt
