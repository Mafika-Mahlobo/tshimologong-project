import os

class Config:
    
    MYSQL_HOST = 'localhost'
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_DB = 'SurveysDB'