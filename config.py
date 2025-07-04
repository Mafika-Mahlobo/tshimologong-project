import os

class Config:
    
    MYSQL_HOST = 'ballast.proxy.rlwy.net'
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_DB = 'railway'
    MYSQL_PORT = 37708