from mysql.connector import Error, IntegrityError
from Tables import conectar_bd 

def insertar_categoria_plato(connection, nombre, codigo_categoria):
    """Inserta una categoría de plato"""
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO CategoriaPlato (nombre, codigo_categoria) VALUES (%s, %s)",
            (nombre, codigo_categoria)
        )
        connection.commit()
        print(f"✓ Categoría '{nombre}' insertada")
    except IntegrityError:
        print(f"✗ La categoría con código '{codigo_categoria}' ya existe")
    except Error as err:
        print(f"✗ Error al insertar categoría: {err}")
    finally:
        cursor.close()

def insertar_plato(connection, nombre, codigo_plato, descripcion, precio, id_categoria, disponible=True, tiempo_preparacion_min=0):
    """Inserta un plato"""
    try:
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO Plato 
               (nombre, codigo_plato, descripcion, precio, id_categoria, disponible, tiempo_preparacion_min)
               VALUES (%s, %s, %s, %s, %s, %s, %s)""",
            (nombre, codigo_plato, descripcion, precio, id_categoria, disponible, tiempo_preparacion_min)
        )
        connection.commit()
        print(f"✓ Plato '{nombre}' insertado")
    except IntegrityError:
        print(f"✗ El plato con código '{codigo_plato}' ya existe")
    except Error as err:
        print(f"✗ Error al insertar plato: {err}")
    finally:
        cursor.close()

def insertar_mesa(connection, codigo_mesa, capacidad, ubicacion="", estado="libre"):
    """Inserta una mesa"""
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Mesa (codigo_mesa, capacidad, ubicacion, estado) VALUES (%s, %s, %s, %s)",
            (codigo_mesa, capacidad, ubicacion, estado)
        )
        connection.commit()
        print(f"✓ Mesa '{codigo_mesa}' insertada")
    except IntegrityError:
        print(f"✗ La mesa con código '{codigo_mesa}' ya existe")
    except Error as err:
        print(f"✗ Error al insertar mesa: {err}")
    finally:
        cursor.close()

def insertar_cliente(connection, codigo_cliente, nombre, telefono, correo):
    """Inserta un cliente"""
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Cliente (codigo_cliente, nombre, telefono, correo) VALUES (%s, %s, %s, %s)",
            (codigo_cliente, nombre, telefono, correo)
        )
        connection.commit()
        print(f"✓ Cliente '{nombre}' insertado")
    except IntegrityError:
        print(f"✗ El cliente con código '{codigo_cliente}' ya existe")
    except Error as err:
        print(f"✗ Error al insertar cliente: {err}")
    finally:
        cursor.close()

def insertar_turno(connection, codigo_turno, fecha, hora_inicio, hora_fin):
    """Inserta un turno"""
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Turno (codigo_turno, fecha, hora_inicio, hora_fin) VALUES (%s, %s, %s, %s)",
            (codigo_turno, fecha, hora_inicio, hora_fin)
        )
        connection.commit()
        print(f"✓ Turno '{codigo_turno}' insertado")
    except IntegrityError:
        print(f"✗ El turno con código '{codigo_turno}' ya existe")
    except Error as err:
        print(f"✗ Error al insertar turno: {err}")
    finally:
        cursor.close()

def insertar_reserva(connection, id_cliente, id_mesa, id_turno, num_personas, fecha_reserva, codigo_reserva, estado, observaciones=None):
    """Inserta una reserva"""
    try:
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO Reserva (id_cliente, id_mesa, id_turno, num_personas, fecha_reserva, codigo_reserva, estado, observaciones)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
            (id_cliente, id_mesa, id_turno, num_personas, fecha_reserva, codigo_reserva, estado, observaciones)
        )
        connection.commit()
        print(f"✓ Reserva '{codigo_reserva}' insertada")
    except IntegrityError:
        print(f"✗ La reserva con código '{codigo_reserva}' ya existe")
    except Error as err:
        print(f"✗ Error al insertar reserva: {err}")
    finally:
        cursor.close()

def insertar_mesero(connection, codigo_mesero, nombre, telefono, correo, id_jefe=None, activo=True):
    """Inserta un mesero"""
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Mesero (codigo_mesero, nombre, telefono, correo, id_jefe, activo) VALUES (%s, %s, %s, %s, %s, %s)",
            (codigo_mesero, nombre, telefono, correo, id_jefe, activo)
        )
        connection.commit()
        print(f"✓ Mesero '{nombre}' insertado")
    except IntegrityError:
        print(f"✗ El mesero con código '{codigo_mesero}' ya existe")
    except Error as err:
        print(f"✗ Error al insertar mesero: {err}")
    finally:
        cursor.close()

def insertar_pedido(connection, id_reserva, id_mesa, codigo_pedido, estado, fecha_pedido, total, id_mesero):
    """Inserta un pedido"""
    try:
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO Pedido (id_reserva, id_mesa, codigo_pedido, estado, fecha_pedido, total, id_mesero)
               VALUES (%s, %s, %s, %s, %s, %s, %s)""",
            (id_reserva, id_mesa, codigo_pedido, estado, fecha_pedido, total, id_mesero)
        )
        connection.commit()
        print(f"✓ Pedido '{codigo_pedido}' insertado")
    except IntegrityError:
        print(f"✗ El pedido con código '{codigo_pedido}' ya existe")
    except Error as err:
        print(f"✗ Error al insertar pedido: {err}")
    finally:
        cursor.close()

def insertar_detalle_pedido(connection, id_pedido, id_plato, codigo_detallePedido, cantidad, precio_unitario):
    """Inserta un detalle de pedido"""
    try:
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO DetallePedido (id_pedido, id_plato, codigo_detallePedido, cantidad, precio_unitario)
               VALUES (%s, %s, %s, %s, %s)""",
            (id_pedido, id_plato, codigo_detallePedido, cantidad, precio_unitario)
        )
        connection.commit()
        print(f"✓ Detalle '{codigo_detallePedido}' insertado")
    except IntegrityError:
        print(f"✗ El detalle con código '{codigo_detallePedido}' ya existe")
    except Error as err:
        print(f"✗ Error al insertar detalle de pedido: {err}")
    finally:
        cursor.close()

def insertar_pago(connection, codigo_pago, id_pedido, fecha_pago, monto, metodo):
    """Inserta un pago"""
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Pago (codigo_pago, id_pedido, fecha_pago, monto, metodo) VALUES (%s, %s, %s, %s, %s)",
            (codigo_pago, id_pedido, fecha_pago, monto, metodo)
        )
        connection.commit()
        print(f"✓ Pago '{codigo_pago}' insertado")
    except IntegrityError:
        print(f"✗ El pago con código '{codigo_pago}' ya existe")
    except Error as err:
        print(f"✗ Error al insertar pago: {err}")
    finally:
        cursor.close()

def insertar_mesero_pedido(connection, id_mesero, id_pedido, rol):
    """Inserta una asignación mesero-pedido"""
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO MeseroPedido (id_mesero, id_pedido, rol) VALUES (%s, %s, %s)",
            (id_mesero, id_pedido, rol)
        )
        connection.commit()
        print(f"✓ Asignación mesero-pedido insertada")
    except IntegrityError:
        print(f"✗ La asignación ya existe")
    except Error as err:
        print(f"✗ Error al insertar mesero-pedido: {err}")
    finally:
        cursor.close()