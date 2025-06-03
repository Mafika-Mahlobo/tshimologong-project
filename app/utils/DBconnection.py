"""
Establish DB connection
"""
from config import Config
from app import app
app.config.from_object(Config)
import psycopg2
from flask import current_app

def get_DBconnection():
    conn = psycopg2.connect(
        host=current_app.config['POSTGRES_HOST'],
        user=current_app.config['POSTGRES_USER'],
        password=current_app.config['POSTGRES_PASSWORD'],
        dbname=current_app.config['POSTGRES_DB']
    )
    return conn
