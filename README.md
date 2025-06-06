# Survey web application

This is a web-based survey portal built using Flask, HTML, CSS, jQuery, and Python.

## Table of Contents
- [Introduction](#Introduction)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#Usage)

## Introduction
This project was built as part of an assessment to prove basic programming principles. Visit my Linkedin provile [here](https://www.linkedin.com/in/mafika-mahlobo-719a9a164/).

## Dependencies
- Flask: Web framework for Python
- jQuery: JavaScript library for simplifying HTML DOM traversal and manipulation
- MYSQL Server
- python-dotenv
- Other Python Dependencies as listed in requirements.txt

## Installation

1. You need to have python3 installed on your machine.

2. Download and install MYSQL (*follow the prompt to create a user account*).

3. Create a .env file in the root folder and save your MYSQL details as shown below.

```bash
MYSQL_USER="your username"
MYSQL_PASSWORD="your password"
```

4. Create Database.

```bash
mysql -u {your usernme} -p < createDB.sql
```

5. Clone the repository to your local machine:
```bash
git clone https://github.com/Mafika-Mahlobo/tshimologong-project
```

6. cd to the project folder
```bash
cd tshimologong-project
```

7. Install more dependencies using the following command or install them manually.

```bash
pip install -r requirements.txt
```

## Usage

- Start the Flask server:

```bash
python3 main.py
```
- Open your web browser and navigate to http://localhost:5000 to access the Survey web application.
