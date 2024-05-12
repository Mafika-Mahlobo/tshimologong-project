# Survey web application

This is a web-based survey portal built using Flask, HTML, CSS, jQuery, and Python.

## Table of Contents
- [Introduction](#Introduction)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#Usage)

## Introduction
This project was built as part of a assessment to prove basic programming principles. visit the source code in my githun profile [here] (https://github.com/Mafika-Mahlobo/tshimologong-project). Also visit my Linkedin provile [here] (https://www.linkedin.com/in/mafika-mahlobo-719a9a164/).

## Dependencies
- Flask: Web framework for Python
- jQuery: JavaScript library for simplifying HTML DOM traversal and manipulation
- MYSQL Sever
- python-dotenv
- Other Python Dependancies as listed in requirements.txt

## Installation

1. You need to have python3 installed on you machine.

2. Download and install MYSQL (*folow prompt to creaet a user account*).

3. Create a .env file in the root folder and save your MYSQL details as shown below.

   ```bash
   MYSQL_USER= #your username
   MYSQL_PASSWORD= #your password
   ```
 Create Database (*you might need to run the command inside MYSQL folder*).

    ```bash
 mysql -u {your usernme} -p < createDB.sql
    ```

4. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Mafika-Mahlobo/tshimologong-project
   ```

5. Cd to the project folder
    ```bash
    cd tshimologong-project
    ```

6. Install more dependacies using the following cammand or install them manually. (*you might need to run the following command in you C drive*)

   ```bash
    pip install -r requirements.txt
   ```

## Usage

- Start the Flask server:
```bash
  python3 main.py
  ```
- Open your web browser and navigate to http://localhost:5000 to access the Library Management System.
