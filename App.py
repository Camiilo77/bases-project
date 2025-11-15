from Tables import (
    conectar_bd,crear_conexion_inicial,DB_CONFIG,create_database, create_table_categoria_plato, create_table_plato,
    create_table_mesa, create_table_cliente, create_table_turno,
    create_table_reserva, create_table_mesero, create_table_pedido,
    create_table_detalle_pedido, create_table_pago
)

from Insertions import (
    insertar_categoria_plato, insertar_plato, insertar_mesa, insertar_cliente,
    insertar_turno, insertar_reserva, insertar_mesero, insertar_pedido,
    insertar_detalle_pedido, insertar_pago
)

def crear_todas_las_tablas():
    create_database()
    conn = conectar_bd()
    create_table_categoria_plato(conn)
    create_table_plato(conn)
    create_table_mesa(conn)
    create_table_cliente(conn)
    create_table_turno(conn)
    create_table_reserva(conn)
    create_table_mesero(conn)
    create_table_pedido(conn)
    create_table_detalle_pedido(conn)
    create_table_pago(conn)
    conn.close()

def insertar_datos_ejemplo():
    conn= conectar_bd()
    # 1. Categoría de platos
    insertar_categoria_plato(conn,  "Entradas", "ENTR")
    insertar_categoria_plato(conn,  "Platos Fuertes", "FUERTE")
    # 2. Platos
    insertar_plato(conn,  "Ensalada César", "PL001", "Lechuga y pollo", 5.50, 1)
    insertar_plato(conn,  "Bistec Asado", "PL002", "Carne con papas", 12.80, 2)
    # 3. Mesas
    insertar_mesa(conn,  "M01", 4)
    insertar_mesa(conn,  "M02", 6)
    # 4. Clientes
    insertar_cliente(conn,  "CLI001", "Ana Gómez", "3131111111", "ana@gmail.com")
    insertar_cliente(conn,  "CLI002", "José Pérez", "3102222222", "jose@gmail.com")
    # 5. Turnos
    insertar_turno(conn,  "TURNO-AM", "2025-11-16", "09:00", "12:00")
    insertar_turno(conn,  "TURNO-PM", "2025-11-16", "19:00", "22:00")
    # 6. Meseros, con jerarquía
    insertar_mesero(conn, "MES001", "Luis Pastor", "3201112233", "luis@restaurante.com")
    insertar_mesero(conn, "MES002", "Carlos Jefe", "3201112244", "carlos@restaurante.com", 1)  # Luis es jefe de Carlos
    # 7. Reservas (Ana reserva mesa M01 en turno 1)
    insertar_reserva(conn, 1, 1, 1, "2025-11-16", "RES001", "confirmada")
    insertar_reserva(conn, 2, 2, 2, "2025-11-16", "RES002", "confirmada")
    # 8. Pedidos (Luis atiende pedido de Ana, Carlos atiende el otro)
    insertar_pedido(conn,  1, "PED001", "2025-11-16", "abierto", 1)
    insertar_pedido(conn,  2, "PED002", "2025-11-16", "abierto", 2)
    # 9. DetallePedido
    insertar_detalle_pedido(conn, 1, 1, "DET001", 2, 5.50) # Ensalada César x2
    insertar_detalle_pedido(conn, 2, 2, "DET002", 1, 12.80) # Bistec Asado x1
    # 10. Pago
    insertar_pago(conn,  "PAG001", 1, "2025-11-16", 11.00, "Efectivo")
    insertar_pago(conn,  "PAG002", 2, "2025-11-16", 12.80, "Tarjeta")
    conn.close()
    print("¡Inserciones de prueba completadas!")

if __name__ == "__main__":
    crear_todas_las_tablas()
    insertar_datos_ejemplo()
