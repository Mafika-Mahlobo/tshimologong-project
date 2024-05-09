import os
from dotenv import load_dotenv

load_dotenv()

MYSQL_HOST = "localhost"
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = "SurveysDB"
