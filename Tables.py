import mysql.connector as msqlC
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "32345",
    "database": "Proyecto_Restaurante"
}

def crear_conexion_inicial():
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
    try:
        connection = msqlC.connect(**DB_CONFIG)
        if connection.is_connected():
            print(f"Conexión exitosa a la base de datos: {connection.database}")
    except Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None
    return connection

def create_table_categoria_plato(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES LIKE 'CategoriaPlato'")
        existe = cursor.fetchone()
        if existe:
            print("La tabla CategoriaPlato ya existe")
        else:
            cursor.execute("""
                CREATE TABLE CategoriaPlato (
                    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
                    codigo_categoria VARCHAR(50) NOT NULL UNIQUE,
                    nombre VARCHAR(50) NOT NULL
                )
            """)
            print("Tabla CategoriaPlato creada exitosamente")
    except Error as err:
        print(f"Error al crear CategoriaPlato: {err}")

def create_table_plato(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES LIKE 'Plato'")
        existe = cursor.fetchone()
        if existe:
            print("La tabla Plato ya existe")
        else:
            cursor.execute("""
                CREATE TABLE Plato (
                    id_plato INT AUTO_INCREMENT PRIMARY KEY,
                    codigo_plato VARCHAR(50) NOT NULL UNIQUE,
                    nombre VARCHAR(50) NOT NULL,
                    descripcion VARCHAR(50),
                    precio DECIMAL(10,4) NOT NULL CHECK (precio >= 0),
                    disponible BOOLEAN NOT NULL DEFAULT TRUE,
                    tiempo_preparacion_min SMALLINT UNSIGNED NOT NULL DEFAULT 0,
                    id_categoria INT,
                    FOREIGN KEY (id_categoria) REFERENCES CategoriaPlato(id_categoria)
                )
            """)
            print("Tabla Plato creada exitosamente")
    except Error as err:
        print(f"Error al crear Plato: {err}")

def create_table_mesa(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES LIKE 'Mesa'")
        existe = cursor.fetchone()
        if existe:
            print("La tabla Mesa ya existe")
        else:
            cursor.execute("""
                CREATE TABLE Mesa (
                    id_mesa INT AUTO_INCREMENT PRIMARY KEY,
                    codigo_mesa VARCHAR(50) NOT NULL UNIQUE,
                    capacidad INT NOT NULL,
                    ubicacion VARCHAR(80),
                    estado ENUM('libre','reservada','ocupada','fuera_servicio') NOT NULL DEFAULT 'libre'
                )
            """)
            print("Tabla Mesa creada exitosamente")
    except Error as err:
        print(f"Error al crear Mesa: {err}")

def create_table_cliente(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES LIKE 'Cliente'")
        existe = cursor.fetchone()
        if existe:
            print("La tabla Cliente ya existe")
        else:
            cursor.execute("""
                CREATE TABLE Cliente (
                    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
                    codigo_cliente VARCHAR(50) NOT NULL UNIQUE,
                    nombre VARCHAR(50) NOT NULL,
                    telefono VARCHAR(50) NOT NULL UNIQUE,
                    correo VARCHAR(50) NULL UNIQUE
                )
            """)
            print("Tabla Cliente creada exitosamente")
    except Error as err:
        print(f"Error al crear Cliente: {err}")

def create_table_turno(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES LIKE 'Turno'")
        existe = cursor.fetchone()
        if existe:
            print("La tabla Turno ya existe")
        else:
            cursor.execute("""
                CREATE TABLE Turno (
                    id_turno INT AUTO_INCREMENT PRIMARY KEY,
                    codigo_turno VARCHAR(50) NOT NULL UNIQUE,
                    fecha DATE NOT NULL,
                    hora_inicio TIME NOT NULL,
                    hora_fin TIME NOT NULL
                )
            """)
            print("Tabla Turno creada exitosamente")
    except Error as err:
        print(f"Error al crear Turno: {err}")

def create_table_reserva(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES LIKE 'Reserva'")
        existe = cursor.fetchone()
        if existe:
            print("La tabla Reserva ya existe")
        else:
            cursor.execute("""
                CREATE TABLE Reserva (
                    id_reserva INT AUTO_INCREMENT PRIMARY KEY,
                    id_cliente INT NOT NULL,
                    id_mesa INT NOT NULL,
                    id_turno INT NOT NULL,
                    num_personas TINYINT UNSIGNED NOT NULL CHECK (num_personas > 0),
                    estado ENUM('pendiente','confirmada','cancelada','en_servicio','finalizada') NOT NULL DEFAULT 'pendiente',
                    fecha_reserva DATE NOT NULL,
                    codigo_reserva VARCHAR(50) NOT NULL UNIQUE,
                    observaciones TEXT,
                    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
                    FOREIGN KEY (id_mesa) REFERENCES Mesa(id_mesa),
                    FOREIGN KEY (id_turno) REFERENCES Turno(id_turno),
                    UNIQUE(id_mesa, id_turno)
                )
            """)
            print("Tabla Reserva creada exitosamente")
    except Error as err:
        print(f"Error al crear Reserva: {err}")

def create_table_mesero(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES LIKE 'Mesero'")
        existe = cursor.fetchone()
        if existe:
            print("La tabla Mesero ya existe")
        else:
            cursor.execute("""
                CREATE TABLE Mesero (
                    id_mesero INT AUTO_INCREMENT PRIMARY KEY,
                    codigo_mesero VARCHAR(50) NOT NULL UNIQUE,
                    nombre VARCHAR(50) NOT NULL,
                    telefono VARCHAR(50) NOT NULL,
                    correo VARCHAR(50) NULL,
                    id_jefe INT NULL,
                    activo BOOLEAN NOT NULL DEFAULT TRUE,
                    FOREIGN KEY (id_jefe) REFERENCES Mesero(id_mesero)
                )
            """)
            print("Tabla Mesero creada exitosamente")
    except Error as err:
        print(f"Error al crear Mesero: {err}")

def create_table_pedido(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES LIKE 'Pedido'")
        existe = cursor.fetchone()
        if existe:
            print("La tabla Pedido ya existe")
        else:
            cursor.execute("""
                CREATE TABLE Pedido (
                    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
                    id_reserva INT NOT NULL,
                    id_mesa INT NOT NULL,  
                    codigo_pedido VARCHAR(50) NOT NULL UNIQUE,
                    estado ENUM('abierto','en_preparacion','servido','cerrado','pagado','anulado') NOT NULL DEFAULT 'abierto',
                    fecha_pedido DATE NOT NULL,
                    total DECIMAL(10,2) NOT NULL DEFAULT 0.00,
                    id_mesero INT NOT NULL,
                    FOREIGN KEY (id_reserva) REFERENCES Reserva(id_reserva),
                    FOREIGN KEY (id_mesero) REFERENCES Mesero(id_mesero),
                    FOREIGN KEY (id_mesa) REFERENCES Mesa(id_mesa)
                )
            """)
            print("Tabla Pedido creada exitosamente")
    except Error as err:
        print(f"Error al crear Pedido: {err}")

def create_table_detalle_pedido(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES LIKE 'DetallePedido'")
        existe = cursor.fetchone()
        if existe:
            print("La tabla DetallePedido ya existe")
        else:
            cursor.execute("""
                CREATE TABLE DetallePedido (
                    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
                    id_pedido INT NOT NULL,
                    id_plato INT NOT NULL,
                    cantidad SMALLINT UNSIGNED NOT NULL CHECK (cantidad > 0),
                    codigo_detallePedido VARCHAR(50) NOT NULL UNIQUE,
                    precio_unitario DECIMAL(10,4) NOT NULL,
                    FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
                    FOREIGN KEY (id_plato) REFERENCES Plato(id_plato)
               
                )
            """)
            print("Tabla DetallePedido creada exitosamente")
    except Error as err:
        print(f"Error al crear DetallePedido: {err}")

def create_table_pago(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES LIKE 'Pago'")
        existe = cursor.fetchone()
        if existe:
            print("La tabla Pago ya existe")
        else:
            cursor.execute("""
                CREATE TABLE Pago (
                    id_pago INT AUTO_INCREMENT PRIMARY KEY,
                    codigo_pago VARCHAR(50) NOT NULL UNIQUE,
                    id_pedido INT NOT NULL,
                    fecha_pago DATE NOT NULL,
                    monto DECIMAL(10,4) NOT NULL CHECK (monto > 0),
                    metodo ENUM('efectivo','tarjeta','pos','transferencia') NOT NULL,
                    FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido)
                )
            """)
            print("Tabla Pago creada exitosamente")
    except Error as err:
        print(f"Error al crear Pago: {err}")


def create_table_mesero_pedido(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES LIKE 'MeseroPedido'")
        existe = cursor.fetchone()
        if existe:
            print("La tabla Pago ya existe")
        else:
         cursor.execute('''
            CREATE TABLE IF NOT EXISTS MeseroPedido (
                id_mesero INT NOT NULL,
                id_pedido INT NOT NULL,
                rol VARCHAR(50),
                primary key (id_mesero, id_pedido),
                FOREIGN KEY (id_mesero) REFERENCES mesero(id_mesero),
                FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido)
            )
        ''')
    except Error as err:
        print(f"Error al crear mesero_pedido: {err}")
    