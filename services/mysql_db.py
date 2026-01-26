import mysql.connector
from config import Config

def create_connection():
    try:
        connection = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASS,
            port=Config.DB_PORT,
            database=Config.DB_NAME
        )
        return connection
    except Exception as e:
        print(e)

