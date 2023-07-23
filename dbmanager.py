import os
import psycopg2
from dotenv import load_dotenv
from psycopg2 import sql

class DBManager:
    def __init__(self) -> None:
        load_dotenv() # take environment variables from .env.
        self.connection = None
    
    def connect(self):
        try:
        # Establecer conexión con la base de datos
            self.connection = psycopg2.connect(
                host=os.getenv('DB_HOST'),
                database=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD')
            )
            print("Conexion Exitosa")
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

conn = DBManager()
conn.connect()
conn.disconnect()
