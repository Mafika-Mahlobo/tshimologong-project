
"""
Esatablish DB connection
"""
from config import Config
from app import app
app.config.from_object(Config)
import mysql.connector
from flask import current_app

def get_DBconnection():
	conn = mysql.connector.connect(
		host=current_app.config['MYSQL_HOST'],
		user=current_app.config['MYSQL_USER'],
		password=current_app.config['MYSQL_PASSWORD'],
		database=current_app.config['MYSQL_DB']
		)
	
	return conn
