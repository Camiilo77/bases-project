#insercciones 

from mysql.connector import Error, IntegrityError

from Tables import conectar_bd 

coneccion = conectar_bd()
def insertar_categoria_plato(connection, nombre, codigo_categoria):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO CategoriaPlato (nombre, codigo_categoria) VALUES (%s, %s)",
            (nombre, codigo_categoria)
        )
        connection.commit()
        print(f"Categoría '{nombre}' insertada exitosamente")
    except IntegrityError:
        print(f"La categoría con código '{codigo_categoria}' ya existe")
    except Error as err:
        print(f"Error al insertar categoría: {err}")

def insertar_plato(connection, nombre, codigo_plato, descripcion, precio, id_categoria):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO Plato 
               (nombre, codigo_plato, descripcion, precio, id_categoria)
               VALUES (%s, %s, %s, %s, %s)""",
            (nombre, codigo_plato, descripcion, precio, id_categoria)
        )
        connection.commit()
        print(f"Plato '{nombre}' insertado exitosamente")
    except IntegrityError:
        print(f"El plato con código '{codigo_plato}' ya existe")
    except Error as err:
        print(f"Error al insertar plato: {err}")

def insertar_mesa(connection, codigo_mesa, capacidad):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Mesa (codigo_mesa, capacidad) VALUES (%s, %s)",
            (codigo_mesa, capacidad)
        )
        connection.commit()
        print(f"Mesa '{codigo_mesa}' insertada exitosamente")
    except IntegrityError:
        print(f"La mesa con código '{codigo_mesa}' ya existe")
    except Error as err:
        print(f"Error al insertar mesa: {err}")

def insertar_cliente(connection, codigo_cliente, nombre, telefono, correo):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Cliente (codigo_cliente, nombre, telefono, correo) VALUES (%s, %s, %s, %s)",
            (codigo_cliente, nombre, telefono, correo)
        )
        connection.commit()
        print(f"Cliente '{nombre}' insertado exitosamente")
    except IntegrityError:
        print(f"El cliente con código '{codigo_cliente}' o teléfono '{telefono}' ya existe")
    except Error as err:
        print(f"Error al insertar cliente: {err}")

def insertar_turno(connection, codigo_turno, fecha, hora_inicio, hora_fin):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Turno (codigo_turno, fecha, hora_inicio, hora_fin) VALUES (%s, %s, %s, %s)",
            (codigo_turno, fecha, hora_inicio, hora_fin)
        )
        connection.commit()
        print(f"Turno '{codigo_turno}' insertado exitosamente")
    except IntegrityError:
        print(f"El turno con código '{codigo_turno}' ya existe")
    except Error as err:
        print(f"Error al insertar turno: {err}")

def insertar_reserva(connection, id_cliente, id_mesa, id_turno, fecha_reserva, codigo_reserva, estado):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO Reserva (id_cliente, id_mesa, id_turno, fecha_reserva, codigo_reserva, estado)
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (id_cliente, id_mesa, id_turno, fecha_reserva, codigo_reserva, estado)
        )
        connection.commit()
        print(f"Reserva '{codigo_reserva}' insertada exitosamente")
    except IntegrityError:
        print(f"La reserva con código '{codigo_reserva}' ya existe")
    except Error as err:
        print(f"Error al insertar reserva: {err}")

def insertar_mesero(connection, codigo_mesero, nombre, telefono, correo, id_jefe=None):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Mesero (codigo_mesero, nombre, telefono, correo, id_jefe) VALUES (%s, %s, %s, %s, %s)",
            (codigo_mesero, nombre, telefono, correo, id_jefe)
        )
        connection.commit()
        print(f"Mesero '{nombre}' insertado exitosamente")
    except IntegrityError:
        print(f"El mesero con código '{codigo_mesero}' ya existe")
    except Error as err:
        print(f"Error al insertar mesero: {err}")

def insertar_pedido(connection, id_reserva, codigo_pedido, fecha_pedido, estado, id_mesero):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO Pedido (id_reserva, codigo_pedido, fecha_pedido, estado, id_mesero)
               VALUES (%s, %s, %s, %s, %s)""",
            (id_reserva, codigo_pedido, fecha_pedido, estado, id_mesero)
        )
        connection.commit()
        print(f"Pedido '{codigo_pedido}' insertado exitosamente")
    except IntegrityError:
        print(f"El pedido con código '{codigo_pedido}' ya existe")
    except Error as err:
        print(f"Error al insertar pedido: {err}")

def insertar_detalle_pedido(connection, id_pedido, id_plato, codigo_detallePedido, cantidad, precio_unitario):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO DetallePedido (id_pedido, id_plato, codigo_detallePedido, cantidad, precio_unitario)
               VALUES (%s, %s, %s, %s, %s)""",
            (id_pedido, id_plato, codigo_detallePedido, cantidad, precio_unitario)
        )
        connection.commit()
        print(f"DetallePedido '{codigo_detallePedido}' insertado exitosamente")
    except IntegrityError:
        print(f"El detalle con código '{codigo_detallePedido}' ya existe")
    except Error as err:
        print(f"Error al insertar detalle pedido: {err}")

def insertar_pago(connection, codigo_pago, id_pedido, fecha_pago, monto, metodo):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO Pago (codigo_pago, id_pedido, fecha_pago, monto, metodo)
               VALUES (%s, %s, %s, %s, %s)""",
            (codigo_pago, id_pedido, fecha_pago, monto, metodo)
        )
        connection.commit()
        print(f"Pago '{codigo_pago}' insertado exitosamente")
    except IntegrityError:
        print(f"El pago con código '{codigo_pago}' ya existe")
    except Error as err:
        print(f"Error al insertar pago: {err}")
