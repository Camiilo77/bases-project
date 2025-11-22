from Tables import (
    conectar_bd, crear_conexion_inicial, DB_CONFIG, create_database, 
    create_table_categoria_plato, create_table_plato, create_table_mesa, 
    create_table_cliente, create_table_turno, create_table_reserva, 
    create_table_mesero, create_table_pedido, create_table_detalle_pedido, 
    create_table_pago, create_table_mesero_pedido
)

from Insertions import (
    insertar_categoria_plato, insertar_plato, insertar_mesa, insertar_cliente,
    insertar_turno, insertar_reserva, insertar_mesero, insertar_pedido,
    insertar_detalle_pedido, insertar_pago, insertar_mesero_pedido
)

def crear_todas_las_tablas():
    """Crea la base de datos y todas las tablas"""
    print("\n" + "="*60)
    print("CREANDO BASE DE DATOS Y TABLAS")
    print("="*60)
    
    create_database()
    conn = conectar_bd()
    
    if conn is None:
        print("❌ No se pudo conectar a la base de datos")
        return
    
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
    create_table_mesero_pedido(conn)
    
    conn.close()
    print("\n✅ Todas las tablas fueron creadas exitosamente\n")


def insertar_datos_completos():
    """Inserta 50 registros en cada tabla"""
    conn = conectar_bd()
    if conn is None:
        print("❌ No se pudo conectar a la base de datos")
        return
    
    print("\n" + "="*60)
    print("INSERTANDO DATOS EN LAS TABLAS")
    print("="*60)
    
    # ========== 1. CATEGORÍAS DE PLATOS (50) ==========
    print("\n📂 Insertando Categorías de Platos...")
    categorias = [
        ("Entradas", "CAT001"), ("Sopas", "CAT002"), ("Ensaladas", "CAT003"),
        ("Carnes Rojas", "CAT004"), ("Pollo", "CAT005"), ("Pescados", "CAT006"),
        ("Mariscos", "CAT007"), ("Pasta", "CAT008"), ("Pizza", "CAT009"),
        ("Hamburguesas", "CAT010"), ("Vegetariano", "CAT011"), ("Vegano", "CAT012"),
        ("Postres Fríos", "CAT013"), ("Postres Calientes", "CAT014"), ("Bebidas Frías", "CAT015"),
        ("Bebidas Calientes", "CAT016"), ("Cócteles", "CAT017"), ("Jugos", "CAT018"),
        ("Desayunos", "CAT019"), ("Brunch", "CAT020"), ("Comida Mexicana", "CAT021"),
        ("Comida Italiana", "CAT022"), ("Comida Asiática", "CAT023"), ("Comida Francesa", "CAT024"),
        ("Comida Española", "CAT025"), ("Comida Japonesa", "CAT026"), ("Comida China", "CAT027"),
        ("Comida Tailandesa", "CAT028"), ("Comida India", "CAT029"), ("Comida Árabe", "CAT030"),
        ("Comida Peruana", "CAT031"), ("Comida Argentina", "CAT032"), ("Tapas", "CAT033"),
        ("Finger Food", "CAT034"), ("Parrilla", "CAT035"), ("BBQ", "CAT036"),
        ("Ahumados", "CAT037"), ("Al Horno", "CAT038"), ("Fritos", "CAT039"),
        ("Horneados", "CAT040"), ("A la Plancha", "CAT041"), ("Guisos", "CAT042"),
        ("Snacks", "CAT043"), ("Aperitivos", "CAT044"), ("Kids Menu", "CAT045"),
        ("Especial Casa", "CAT046"), ("Chef Signature", "CAT047"), ("Temporada", "CAT048"),
        ("Light", "CAT049"), ("Sin Gluten", "CAT050")
    ]
    for nombre, codigo in categorias:
        insertar_categoria_plato(conn, nombre, codigo)
    
    # ========== 2. PLATOS (50) ==========
    print("\n🍽️ Insertando Platos...")
    platos = [
        ("Bruschetta Italiana", "PL001", "Pan con tomate, albahaca y aceite", 12.50, 1, True, 10),
        ("Sopa de Cebolla", "PL002", "Gratinada con queso gruyere", 15.00, 2, True, 20),
        ("Ensalada César", "PL003", "Lechuga, pollo, parmesano, crutones", 18.00, 3, True, 15),
        ("Filete de Res", "PL004", "300g con papas y vegetales", 45.00, 4, True, 30),
        ("Pollo al Horno", "PL005", "Medio pollo con hierbas", 28.00, 5, True, 40),
        ("Salmón a la Parrilla", "PL006", "Con salsa de eneldo", 38.00, 6, True, 25),
        ("Camarones al Ajillo", "PL007", "6 piezas en salsa de ajo", 32.00, 7, True, 15),
        ("Pasta Carbonara", "PL008", "Con tocino y crema", 22.00, 8, True, 18),
        ("Pizza Margarita", "PL009", "Tomate, mozzarella, albahaca", 25.00, 9, True, 20),
        ("Hamburguesa Clásica", "PL010", "200g con queso y papas", 20.00, 10, True, 15),
        ("Lasagna Vegetariana", "PL011", "Con vegetales y bechamel", 24.00, 11, True, 30),
        ("Bowl Vegano", "PL012", "Quinoa, aguacate, garbanzos", 19.00, 12, True, 12),
        ("Helado Artesanal", "PL013", "3 bolas sabores variados", 10.00, 13, True, 5),
        ("Brownie con Helado", "PL014", "Caliente con helado de vainilla", 12.00, 14, True, 8),
        ("Limonada Natural", "PL015", "Recién exprimida", 6.00, 15, True, 5),
        ("Café Espresso", "PL016", "Doble shot", 4.50, 16, True, 3),
        ("Mojito Clásico", "PL017", "Ron, menta, lima", 14.00, 17, True, 7),
        ("Jugo de Naranja", "PL018", "Natural recién exprimido", 7.00, 18, True, 5),
        ("Huevos Rancheros", "PL019", "Con frijoles y tortillas", 16.00, 19, True, 15),
        ("Pancakes", "PL020", "Stack de 3 con miel y frutas", 14.00, 20, True, 12),
        ("Tacos al Pastor", "PL021", "3 tacos con piña", 18.00, 21, True, 15),
        ("Risotto de Hongos", "PL022", "Con parmesano", 26.00, 22, True, 25),
        ("Pad Thai", "PL023", "Fideos con camarones", 23.00, 23, True, 20),
        ("Coq au Vin", "PL024", "Pollo en vino tinto", 35.00, 24, True, 45),
        ("Paella Valenciana", "PL025", "Para 2 personas", 55.00, 25, True, 40),
        ("Sushi Variado", "PL026", "12 piezas mixtas", 32.00, 26, True, 20),
        ("Chow Mein", "PL027", "Fideos salteados con pollo", 19.00, 27, True, 15),
        ("Tom Yum", "PL028", "Sopa picante tailandesa", 17.00, 28, True, 18),
        ("Curry de Pollo", "PL029", "Estilo indio con arroz", 21.00, 29, True, 25),
        ("Falafel Plate", "PL030", "Con hummus y pan pita", 16.00, 30, True, 12),
        ("Ceviche Peruano", "PL031", "Pescado fresco en limón", 27.00, 31, True, 15),
        ("Bife de Chorizo", "PL032", "350g estilo argentino", 48.00, 32, True, 25),
        ("Patatas Bravas", "PL033", "Con salsa brava", 11.00, 33, True, 10),
        ("Mini Burgers", "PL034", "6 piezas variadas", 22.00, 34, True, 15),
        ("Parrillada Mixta", "PL035", "Carnes variadas para 2", 65.00, 35, True, 35),
        ("Costillas BBQ", "PL036", "Rack completo", 42.00, 36, True, 40),
        ("Salmón Ahumado", "PL037", "Con alcaparras y cebolla", 29.00, 37, True, 8),
        ("Pollo al Horno Especial", "PL038", "Con papas doradas", 31.00, 38, True, 35),
        ("Calamares Fritos", "PL039", "Con salsa tártara", 24.00, 39, True, 12),
        ("Pan de Ajo", "PL040", "6 rebanadas", 8.00, 40, True, 8),
        ("Pescado a la Plancha", "PL041", "Con vegetales", 33.00, 41, True, 20),
        ("Estofado de Res", "PL042", "Con papas y zanahorias", 28.00, 42, True, 50),
        ("Nachos Supreme", "PL043", "Con queso, guacamole y crema", 15.00, 43, True, 10),
        ("Tabla de Quesos", "PL044", "5 quesos artesanales", 26.00, 44, True, 5),
        ("Nuggets de Pollo", "PL045", "8 piezas con papas", 13.00, 45, True, 12),
        ("Pulpo a la Gallega", "PL046", "Especialidad de la casa", 39.00, 46, True, 30),
        ("Cordero al Romero", "PL047", "Firma del chef", 52.00, 47, True, 45),
        ("Trucha de Temporada", "PL048", "Según mercado", 34.00, 48, True, 25),
        ("Ensalada Detox", "PL049", "Mix de hojas verdes", 17.00, 49, True, 8),
        ("Pasta Sin Gluten", "PL050", "Penne con salsa marinara", 23.00, 50, True, 18)
    ]
    for nombre, codigo, desc, precio, cat, disp, tiempo in platos:
        insertar_plato(conn, nombre, codigo, desc, precio, cat, disp, tiempo)
    
    # ========== 3. MESAS (50) ==========
    print("\n🪑 Insertando Mesas...")
    ubicaciones = ["Terraza", "Interior Ventana", "Interior Centro", "VIP", "Bar", "Patio", "Salón Principal"]
    estados = ["libre", "reservada", "ocupada", "libre"]
    for i in range(1, 51):
        codigo = f"M{i:03d}"
        capacidad = 2 if i <= 20 else (4 if i <= 40 else 6)
        ubicacion = ubicaciones[i % len(ubicaciones)]
        estado = estados[i % len(estados)]
        insertar_mesa(conn, codigo, capacidad, ubicacion, estado)
    
    # ========== 4. CLIENTES (50) ==========
    print("\n👥 Insertando Clientes...")
    nombres = [
        "Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Luis Rodríguez",
        "Laura Fernández", "Pedro Gómez", "Carmen Díaz", "José Hernández", "Isabel Ruiz",
        "Francisco Moreno", "Teresa Jiménez", "Antonio Álvarez", "Dolores Romero", "Manuel Sanz",
        "Rosa Navarro", "Miguel Torres", "Pilar Ramírez", "Javier Gil", "Lucía Serrano",
        "David Blanco", "Elena Molina", "Daniel Castro", "Sara Ortiz", "Alejandro Rubio",
        "Marta Delgado", "Pablo Iglesias", "Julia Ortega", "Sergio Morales", "Beatriz Núñez",
        "Raúl Guerrero", "Cristina Prieto", "Alberto Lozano", "Natalia Méndez", "Víctor Cruz",
        "Patricia Flores", "Roberto Herrera", "Silvia Gallego", "Fernando Vega", "Andrea Campos",
        "Marcos Carrasco", "Claudia Reyes", "Adrián Vázquez", "Diana Cortés", "Óscar Medina",
        "Verónica Aguilar", "Ricardo León", "Sofía Fuentes", "Guillermo Santos", "Marina Cabrera"
    ]
    for i, nombre in enumerate(nombres, 1):
        codigo = f"CLI{i:03d}"
        telefono = f"+52155{1000+i:04d}{i:04d}"
        correo = f"cliente{i}@email.com"
        insertar_cliente(conn, codigo, nombre, telefono, correo)
    
    # ========== 5. TURNOS (50) ==========
    print("\n⏰ Insertando Turnos...")
    from datetime import date, time, timedelta
    fecha_base = date(2024, 11, 1)
    turnos_tipo = [
        ("Desayuno", time(7, 0), time(11, 0)),
        ("Almuerzo", time(12, 0), time(16, 0)),
        ("Cena", time(18, 0), time(23, 0))
    ]
    contador = 1
    for dia in range(17):  # 17 días para tener más de 50 turnos
        fecha = fecha_base + timedelta(days=dia)
        for tipo, inicio, fin in turnos_tipo:
            if contador > 50:
                break
            codigo = f"TUR{contador:03d}"
            insertar_turno(conn, codigo, fecha, inicio, fin)
            contador += 1
        if contador > 50:
            break
    
    # ========== 6. MESEROS (50) ==========
    print("\n👔 Insertando Meseros...")
    nombres_meseros = [
        "Alberto Sánchez", "Mónica Pérez", "Raúl Torres", "Gabriela López", "Iván Martín",
        "Valeria Castro", "Diego Romero", "Camila Vega", "Andrés Núñez", "Daniela Ramos",
        "Sebastián Flores", "Lorena Gil", "Martín Cruz", "Paula Ortiz", "Ernesto Díaz",
        "Carolina Mora", "Felipe Ruiz", "Alejandra Soto", "Rodrigo Peña", "Vanessa Luna",
        "Gustavo Ríos", "Paola Mendoza", "Julián Vargas", "Sandra Herrera", "Esteban Silva",
        "Jessica Campos", "Mauricio Rojas", "Fernanda Guzmán", "Leonardo Bravo", "Mariana Medina",
        "Héctor Castillo", "Liliana Acosta", "Armando Paredes", "Rocío Navarro", "César Aguilar",
        "Guadalupe Muñoz", "Ángel Reyes", "Susana Morales", "Ramiro Ibarra", "Olivia Serrano",
        "Enrique Delgado", "Jimena Cortés", "Arturo Fuentes", "Estrella Benítez", "Tomás Salazar",
        "Regina Pacheco", "Ignacio Lara", "Adriana Carrillo", "Gonzalo Espinoza", "Marisol Domínguez"
    ]
    # Primeros 5 son jefes (sin id_jefe)
    for i in range(1, 6):
        codigo = f"MES{i:03d}"
        insertar_mesero(conn, codigo, nombres_meseros[i-1], f"+52155{2000+i:04d}{i:04d}", 
                       f"mesero{i}@restaurante.com", None, True)
    
    # Resto son meseros regulares con jefe asignado
    for i in range(6, 51):
        codigo = f"MES{i:03d}"
        id_jefe = ((i-6) % 5) + 1  # Asigna a uno de los 5 jefes
        insertar_mesero(conn, codigo, nombres_meseros[i-1], f"+52155{2000+i:04d}{i:04d}",
                       f"mesero{i}@restaurante.com", id_jefe, True)
    
    # ========== 7. RESERVAS (50) ==========
    print("\n📅 Insertando Reservas...")
    estados_reserva = ["confirmada", "pendiente", "en_servicio", "finalizada"]
    for i in range(1, 51):
        codigo = f"RES{i:03d}"
        id_cliente = i
        id_mesa = i
        id_turno = i
        num_personas = 2 if i <= 20 else (4 if i <= 40 else 6)
        fecha_reserva = fecha_base + timedelta(days=(i-1) // 3)
        estado = estados_reserva[i % len(estados_reserva)]
        obs = "Sin observaciones" if i % 3 == 0 else None
        insertar_reserva(conn, id_cliente, id_mesa, id_turno, num_personas, 
                        fecha_reserva, codigo, estado, obs)
    
    # ========== 8. PEDIDOS (50) ==========
    print("\n📝 Insertando Pedidos...")
    estados_pedido = ["abierto", "en_preparacion", "servido", "cerrado", "pagado"]
    for i in range(1, 51):
        codigo = f"PED{i:03d}"
        id_reserva = i
        id_mesa = i
        estado = estados_pedido[i % len(estados_pedido)]
        fecha_pedido = fecha_base + timedelta(days=(i-1) // 3)
        total = round(50.00 + (i * 10.5), 2)
        id_mesero = ((i-1) % 50) + 1
        insertar_pedido(conn, id_reserva, id_mesa, codigo, estado, fecha_pedido, total, id_mesero)
    
    # ========== 9. DETALLE PEDIDOS (50) ==========
    print("\n📋 Insertando Detalles de Pedidos...")
    for i in range(1, 51):
        codigo = f"DET{i:03d}"
        id_pedido = i
        id_plato = ((i-1) % 50) + 1
        cantidad = 1 if i % 3 == 0 else (2 if i % 3 == 1 else 3)
        precio_unitario = round(10.00 + (i * 0.75), 2)
        insertar_detalle_pedido(conn, id_pedido, id_plato, codigo, cantidad, precio_unitario)
    
    # ========== 10. PAGOS (50) ==========
    print("\n💳 Insertando Pagos...")
    metodos = ["efectivo", "tarjeta", "pos", "transferencia"]
    for i in range(1, 51):
        codigo = f"PAG{i:03d}"
        id_pedido = i
        fecha_pago = fecha_base + timedelta(days=(i-1) // 3)
        monto = round(50.00 + (i * 10.5), 2)
        metodo = metodos[i % len(metodos)]
        insertar_pago(conn, codigo, id_pedido, fecha_pago, monto, metodo)
    
    # ========== 11. MESERO_PEDIDO (50) ==========
    print("\n🔗 Insertando Mesero-Pedido...")
    roles = ["Principal", "Asistente", "Ayudante", "Soporte"]
    for i in range(1, 51):
        id_mesero = ((i-1) % 50) + 1
        id_pedido = i
        rol = roles[i % len(roles)]
        insertar_mesero_pedido(conn, id_mesero, id_pedido, rol)
    
    conn.close()
    print("\n" + "="*60)
    print("✅ INSERCIÓN DE DATOS COMPLETADA")
    print("="*60)


if __name__ == "__main__":
    print("\n" + "$"*60)
    print("SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("$"*60)
    
    # Crear tablas e insertar datos
    crear_todas_las_tablas()
    insertar_datos_completos()
    
    print("\n" + ":3"*60)
    print("PROCESO COMPLETADO EXITOSAMENTE")
    print(":3"*60)

