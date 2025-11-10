# Tablas

import mysql.connector as msqlC
from mysql.connector import Error, IntegrityError


# configurar conexion

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "bases-project"
}

# conexión a la base de datos

def crear_conexion_inicial():
    """Crea conexión inicial sin seleccionar base de datos (para crearla si no existe)."""
    try:
        connection = msqlC.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"]
        )
        if connection.is_connected():
            print("Conexión exitosa al servidor MySQL")
    except Error as err:
        print(f"Error al conectar al servidor: {err}")
        return None
    return connection

def create_database():
    """Crea la base de datos si no existe."""
    connection = crear_conexion_inicial()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
        print("Base de datos creada o verificada exitosamente")
    except Error as err:
        print(f"Error al crear la base de datos: {err}")
    finally:
        cursor.close()
        connection.close()

def conectar_bd():
    """Conecta directamente a la base de datos ya existente."""
    try:
        connection = msqlC.connect(**DB_CONFIG)
        if connection.is_connected():
            print(f"Conexión exitosa a la base de datos: {connection.database}")
    except Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None
    return connection

