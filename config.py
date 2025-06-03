import os

class Config:
    POSTGRES_HOST = os.getenv("DB_HOST")
    POSTGRES_DB = os.getenv("DB_NAME")
    POSTGRES_USER = os.getenv("DB_USER")
    POSTGRES_PASSWORD = os.getenv("DB_PASSWORD")
