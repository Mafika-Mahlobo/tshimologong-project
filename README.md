# Survey web application

This is a web-based survey portal, built using Flask, HTML, CSS, jQuery, and Python.

## Table of Contents
- [Introduction](#Introduction)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#Usage)

## Introduction
This project was built as part of an assessment to prove basic programming principles. Visit my Linkedin profile [here](https://www.linkedin.com/in/mafika-mahlobo-719a9a164/).

## Dependencies
- Flask: Web framework for Python
- Jquery: JavaScript library for simplifying HTML DOM traversal and manipulation
- MYSQL Sever
- Other Python libraries as listed in requirements.txt

## Installation

1. You need to have python3 installed on your machine.

2. Download and install MYSQL (*follow prompt to create a user account*).

3. Create Database (*you might need to run the command inside MYSQL folder*).
   ```bash
   mysql -u {your usernme} -p < createDB.sql
   ```

5. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Mafika-Mahlobo/tshimologong-project
   ```

6. Cd to the project folder
    ```bash
    cd tshimologong-project
    ```

5. Install more dependancies using the following command or install manually. (*you might need to run the following command in you C drive*)

   ```bash
    pip install -r requirements.txt
   ```

## Usage

- Start the Flask server:
```bash
  python3 app.py
  ```
- Open your web browser and navigate to http://localhost:5000 to access the Library Management System.
