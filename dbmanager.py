import os
import psycopg2
from dotenv import load_dotenv
from psycopg2 import sql


class DataBaseManagement:
    load_dotenv() # take environment variables from .env.
    try:
    # Establecer conexión con la base de datos
        connection = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )

        cursor = connection.cursor()

        # Crear la consulta SQL
        insert_query = sql.SQL("""
            INSERT INTO nombre_tabla (columna1, columna2, columna3)
            VALUES (%s, %s, %s)
        """)

        # Datos a insertar
        data = ("valor1", "valor2", "valor3")

        # Ejecutar la consulta SQL
        cursor.execute(insert_query, data)

        # Hacer commit de la transacción
        connection.commit()

        print("Datos insertados exitosamente")

    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
        # Cerrar la conexión
        if connection:
            cursor.close()
            connection.close()