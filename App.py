from Tables import (
    conectar_bd,crear_conexion_inicial,DB_CONFIG,create_database, create_table_categoria_plato, create_table_plato,
    create_table_mesa, create_table_cliente, create_table_turno,
    create_table_reserva, create_table_mesero, create_table_pedido,
    create_table_detalle_pedido, create_table_pago, create_table_mesero_pedido
)

from Insertions import (
    insertar_categoria_plato, insertar_plato, insertar_mesa, insertar_cliente,
    insertar_turno, insertar_reserva, insertar_mesero, insertar_pedido,
    insertar_detalle_pedido, insertar_pago, insertar_mesero_pedido
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
    create_table_mesero_pedido(conn)
    conn.close()

def insertar_datos_completos():
    """Inserta 40 registros en cada tabla"""
    conn = conectar_bd()
    
    # 1. CATEGORÍAS (40)
    categorias = [
        ("Mariscos", "MAR"), ("Pasta", "PAS"), ("Pollo", "POL"), ("Ensaladas", "ENS"),
        ("Sopas", "SOP"), ("Pescado", "PES"), ("Carnes", "CAR"), ("Hamburguesas", "HAM"),
        ("Pizza", "PIZ"), ("Mexicana", "MEX"), ("Bebidas Naturales", "BEB"), ("Cafés", "CAF"),
        ("Postres", "POS"), ("Empanadas", "EMP"), ("Wraps", "WRA"), ("Peruano", "PER"),
        ("Arepas", "ARP"), ("Sushi", "SUS"), ("Asiática", "ASI"), ("BBQ", "BBQ"),
        ("Acompañamientos", "ACP"), ("Desayuno", "DES"), ("Vegano", "VEG"), ("Italianos", "ITA"),
        ("Sándwiches", "SAN"), ("Helados", "HEL"), ("Tapas", "TAP"), ("Arroces", "ARR"),
        ("Cevichería", "CEV"), ("Parrilla", "PAR"), ("Freidora", "FRE"), ("Alitas", "ALI"),
        ("Brochetas", "BRO"), ("Ensalada Caliente", "ENC"), ("Fideos", "FID"), ("Guisos", "GUI"),
        ("Mollejas", "MOL"), ("Mondongo", "MON"), ("Pato", "PAT"), ("Conejo", "CON")
    ]
    
    print("Insertando 40 categorías...")
    for nombre, codigo in categorias:
        insertar_categoria_plato(conn, nombre, codigo)
    
    # 2. PLATOS (40)
    platos = [
        ('Camarones al ajillo', 'PLT001', 'Camarones frescos salteados en aceite de oliva', 15.99, 1),
        ('Arroz con mariscos', 'PLT002', 'Arroz cremoso con mezcla de mariscos frescos', 18.50, 1),
        ('Pasta alfredo', 'PLT003', 'Fettuccine en salsa cremosa de queso parmesano', 12.90, 2),
        ('Pollo a la plancha', 'PLT004', 'Pechuga de pollo jugosa con especias caseras', 11.50, 3),
        ('Ensalada césar', 'PLT005', 'Lechuga, crotones, queso parmesano y aderezo césar', 9.99, 4),
        ('Sopa de tomate', 'PLT006', 'Sopa cremosa de tomate con especias italianas', 7.50, 5),
        ('Filete de salmón', 'PLT007', 'Salmón al horno con limón y eneldo', 19.99, 6),
        ('Hamburguesa clásica', 'PLT008', 'Carne 100% angus con queso y vegetales frescos', 10.50, 8),
        ('Pizza margarita', 'PLT009', 'Pizza artesanal con mozzarella y albahaca', 13.40, 9),
        ('Tacos mexicanos', 'PLT010', 'Tortillas rellenas con carne marinada y vegetales', 9.70, 10),
        ('Batido de mango', 'PLT011', 'Batido natural preparado con mango fresco', 5.20, 11),
        ('Café latte', 'PLT012', 'Café espresso con leche espumada', 3.90, 12),
        ('Cheesecake de fresa', 'PLT013', 'Postre cremoso con salsa de fresa natural', 6.80, 13),
        ('Empanadas caseras', 'PLT014', 'Empanadas fritas rellenas de carne o pollo', 4.50, 14),
        ('Wrap de pollo', 'PLT015', 'Tortilla rellena de pollo asado y vegetales', 8.20, 15),
        ('Lomo saltado', 'PLT016', 'Carne salteada con cebolla, tomate y papas', 14.30, 7),
        ('Arepa rellena', 'PLT017', 'Arepa rellena con queso y jamón', 5.60, 17),
        ('Sushi mixto', 'PLT018', 'Rollos de sushi con salmón, camarón y cangrejo', 17.20, 18),
        ('Ramen japonés', 'PLT019', 'Caldo tradicional japonés con fideos y toppings', 13.80, 19),
        ('Arroz frito oriental', 'PLT020', 'Arroz salteado con vegetales y salsa de soya', 9.30, 20),
        ('Costillas BBQ', 'PLT021', 'Costillas de cerdo bañadas en salsa BBQ', 16.90, 21),
        ('Papas gratinadas', 'PLT022', 'Papas horneadas con crema y queso fundido', 7.40, 21),
        ('Tostadas francesas', 'PLT023', 'Pan dulce bañado en huevo y canela', 8.10, 22),
        ('Bowl vegano', 'PLT024', 'Mezcla de quinoa, tofu y vegetales frescos', 10.90, 23),
        ('Canelones rellenos', 'PLT025', 'Pasta rellena de carne con salsa bechamel', 14.99, 24),
        ('Sándwich premium', 'PLT026', 'Pan artesanal con jamón, queso y vegetales', 9.80, 25),
        ('Helado artesanal', 'PLT027', 'Helado preparado con frutas naturales', 4.90, 26),
        ('Camarones empanizados', 'PLT028', 'Camarones acompañados de salsa tártara', 16.20, 1),
        ('Pechuga rellena', 'PLT029', 'Pollo relleno de queso y espinaca', 13.50, 3),
        ('Crema de champiñones', 'PLT030', 'Crema suave de champiñones frescos', 7.80, 5),
        ('Nuggets caseros', 'PLT031', 'Nuggets de pollo empanizados artesanalmente', 6.40, 8),
        ('Té chai', 'PLT032', 'Infusión de especias con leche', 3.50, 12),
        ('Brownie con helado', 'PLT033', 'Brownie caliente con bola de helado', 6.60, 13),
        ('Bebida de maracuyá', 'PLT034', 'Jugo natural de maracuyá sin azúcar añadida', 5.00, 11),
        ('Panini italiano', 'PLT035', 'Pan tostado con pepperoni y queso mozzarella', 9.60, 24),
        ('Pasta boloñesa', 'PLT036', 'Espaguetis con salsa de carne tradicional', 12.40, 2),
        ('Churrasco premium', 'PLT037', 'Corte de carne jugoso asado a la parrilla', 18.80, 7),
        ('Ceviche peruano', 'PLT038', 'Pescado fresco marinado en limón con cebolla', 15.10, 6),
        ('Waffles con miel', 'PLT039', 'Waffles suaves con miel y frutas', 7.90, 22),
        ('Pollo teriyaki', 'PLT040', 'Pollo salteado con salsa teriyaki y vegetales', 13.20, 19),
    ]
    
    print("Insertando 40 platos...")
    for nombre, codigo, descripcion, precio, id_categoria in platos:
        insertar_plato(conn, nombre, codigo, descripcion, precio, id_categoria)
    
    # 3. MESAS (40)
    mesas = [
        ("M01", 2), ("M02", 2), ("M03", 4), ("M04", 4), ("M05", 4),
        ("M06", 6), ("M07", 6), ("M08", 8), ("M09", 8), ("M10", 10),
        ("M11", 2), ("M12", 4), ("M13", 6), ("M14", 8), ("M15", 10),
        ("M16", 2), ("M17", 4), ("M18", 6), ("M19", 8), ("M20", 10),
        ("M21", 2), ("M22", 4), ("M23", 6), ("M24", 8), ("M25", 10),
        ("M26", 2), ("M27", 4), ("M28", 6), ("M29", 8), ("M30", 10),
        ("M31", 2), ("M32", 4), ("M33", 6), ("M34", 8), ("M35", 10),
        ("M36", 2), ("M37", 4), ("M38", 6), ("M39", 8), ("M40", 10),
    ]
    
    print("Insertando 40 mesas...")
    for codigo, capacidad in mesas:
        insertar_mesa(conn, codigo, capacidad)
    
    # 4. CLIENTES (40)
    clientes = [
        ("CLI001", "Ana Gómez", "3131111111", "ana@gmail.com"),
        ("CLI002", "José Pérez", "3102222222", "jose@gmail.com"),
        ("CLI003", "María López", "3103333333", "maria@gmail.com"),
        ("CLI004", "Carlos Rodríguez", "3104444444", "carlos@gmail.com"),
        ("CLI005", "Laura García", "3105555555", "laura@gmail.com"),
        ("CLI006", "Juan Martínez", "3106666666", "juan@gmail.com"),
        ("CLI007", "Sandra Díaz", "3107777777", "sandra@gmail.com"),
        ("CLI008", "Roberto Sánchez", "3108888888", "roberto@gmail.com"),
        ("CLI009", "Patricia Ramírez", "3109999999", "patricia@gmail.com"),
        ("CLI010", "Miguel Hernández", "3100000000", "miguel@gmail.com"),
        ("CLI011", "Elena Cabrera", "3201111111", "elena@gmail.com"),
        ("CLI012", "David Moreno", "3202222222", "david@gmail.com"),
        ("CLI013", "Gloria Jiménez", "3203333333", "gloria@gmail.com"),
        ("CLI014", "Fernando Ortiz", "3204444444", "fernando@gmail.com"),
        ("CLI015", "Beatriz Navarro", "3205555555", "beatriz@gmail.com"),
        ("CLI016", "Alejandro Castro", "3206666666", "alejandro@gmail.com"),
        ("CLI017", "Sofía Medina", "3207777777", "sofia@gmail.com"),
        ("CLI018", "Raúl Vargas", "3208888888", "raul@gmail.com"),
        ("CLI019", "Verónica Flores", "3209999999", "veronica@gmail.com"),
        ("CLI020", "Andrés Reyes", "3210000000", "andres@gmail.com"),
        ("CLI021", "Camila Ruiz", "3211111111", "camila@gmail.com"),
        ("CLI022", "Diego Herrera", "3212222222", "diego@gmail.com"),
        ("CLI023", "Isabela Soto", "3213333333", "isabela@gmail.com"),
        ("CLI024", "Francisco Vega", "3214444444", "francisco@gmail.com"),
        ("CLI025", "Valentina Silva", "3215555555", "valentina@gmail.com"),
        ("CLI026", "Ricardo Ponce", "3216666666", "ricardo@gmail.com"),
        ("CLI027", "Adriana Cruz", "3217777777", "adriana@gmail.com"),
        ("CLI028", "Gustavo Mora", "3218888888", "gustavo@gmail.com"),
        ("CLI029", "Marcela Navarro", "3219999999", "marcela@gmail.com"),
        ("CLI030", "Javier Romero", "3220000000", "javier@gmail.com"),
        ("CLI031", "Catalina Parra", "3221111111", "catalina@gmail.com"),
        ("CLI032", "Sergio Fuentes", "3222222222", "sergio@gmail.com"),
        ("CLI033", "Daniela Rojas", "3223333333", "daniela@gmail.com"),
        ("CLI034", "Mateo Durán", "3224444444", "mateo@gmail.com"),
        ("CLI035", "Paula Araya", "3225555555", "paula@gmail.com"),
        ("CLI036", "Nicolás Salazar", "3226666666", "nicolas@gmail.com"),
        ("CLI037", "Magdalena Vásquez", "3227777777", "magdalena@gmail.com"),
        ("CLI038", "Enrique Molina", "3228888888", "enrique@gmail.com"),
        ("CLI039", "Antonia Valenzuela", "3229999999", "antonia@gmail.com"),
        ("CLI040", "Tomás Sepúlveda", "3230000000", "tomas@gmail.com"),
    ]
    
    print("Insertando 40 clientes...")
    for codigo, nombre, telefono, correo in clientes:
        insertar_cliente(conn, codigo, nombre, telefono, correo)
    
    # 5. TURNOS (40)
    turnos = [
        ("TURNO-AM-1", "2025-11-18", "09:00", "12:00"),
        ("TURNO-PM-1", "2025-11-18", "12:30", "15:30"),
        ("TURNO-NOCHE-1", "2025-11-18", "18:00", "22:00"),
        ("TURNO-AM-2", "2025-11-19", "09:00", "12:00"),
        ("TURNO-PM-2", "2025-11-19", "12:30", "15:30"),
        ("TURNO-NOCHE-2", "2025-11-19", "18:00", "22:00"),
        ("TURNO-AM-3", "2025-11-20", "09:00", "12:00"),
        ("TURNO-PM-3", "2025-11-20", "12:30", "15:30"),
        ("TURNO-NOCHE-3", "2025-11-20", "18:00", "22:00"),
        ("TURNO-AM-4", "2025-11-21", "09:00", "12:00"),
        ("TURNO-PM-4", "2025-11-21", "12:30", "15:30"),
        ("TURNO-NOCHE-4", "2025-11-21", "18:00", "22:00"),
        ("TURNO-AM-5", "2025-11-22", "09:00", "12:00"),
        ("TURNO-PM-5", "2025-11-22", "12:30", "15:30"),
        ("TURNO-NOCHE-5", "2025-11-22", "18:00", "22:00"),
        ("TURNO-AM-6", "2025-11-23", "09:00", "12:00"),
        ("TURNO-PM-6", "2025-11-23", "12:30", "15:30"),
        ("TURNO-NOCHE-6", "2025-11-23", "18:00", "22:00"),
        ("TURNO-AM-7", "2025-11-24", "09:00", "12:00"),
        ("TURNO-PM-7", "2025-11-24", "12:30", "15:30"),
        ("TURNO-NOCHE-7", "2025-11-24", "18:00", "22:00"),
        ("TURNO-AM-8", "2025-11-25", "09:00", "12:00"),
        ("TURNO-PM-8", "2025-11-25", "12:30", "15:30"),
        ("TURNO-NOCHE-8", "2025-11-25", "18:00", "22:00"),
        ("TURNO-AM-9", "2025-11-26", "09:00", "12:00"),
        ("TURNO-PM-9", "2025-11-26", "12:30", "15:30"),
        ("TURNO-NOCHE-9", "2025-11-26", "18:00", "22:00"),
        ("TURNO-AM-10", "2025-11-27", "09:00", "12:00"),
        ("TURNO-PM-10", "2025-11-27", "12:30", "15:30"),
        ("TURNO-NOCHE-10", "2025-11-27", "18:00", "22:00"),
        ("TURNO-AM-11", "2025-11-28", "09:00", "12:00"),
        ("TURNO-PM-11", "2025-11-28", "12:30", "15:30"),
        ("TURNO-NOCHE-11", "2025-11-28", "18:00", "22:00"),
        ("TURNO-AM-12", "2025-11-29", "09:00", "12:00"),
        ("TURNO-PM-12", "2025-11-29", "12:30", "15:30"),
        ("TURNO-NOCHE-12", "2025-11-29", "18:00", "22:00"),
        ("TURNO-AM-13", "2025-11-30", "09:00", "12:00"),
        ("TURNO-PM-13", "2025-11-30", "12:30", "15:30"),
        ("TURNO-NOCHE-13", "2025-11-30", "18:00", "22:00"),
        ("TURNO-ESPECIAL-1", "2025-12-01", "10:00", "14:00"),
    ]
    
    print("Insertando 40 turnos...")
    for codigo, fecha, hora_inicio, hora_fin in turnos:
        insertar_turno(conn, codigo, fecha, hora_inicio, hora_fin)
    
    # 6. MESEROS (40)
    meseros = [
        ("MES001", "Luis Pastor", "3201112233", "luis@restaurante.com", None),
        ("MES002", "Carlos Jefe", "3201112244", "carlos@restaurante.com", 1),
        ("MES003", "Juan Pérez", "3201112255", "juan.perez@restaurante.com", 2),
        ("MES004", "María González", "3201112266", "maria.gonzalez@restaurante.com", 2),
        ("MES005", "Roberto Díaz", "3201112277", "roberto.diaz@restaurante.com", 1),
        ("MES006", "Sandra López", "3201112288", "sandra.lopez@restaurante.com", 5),
        ("MES007", "Andrés Martínez", "3201112299", "andres.martinez@restaurante.com", 5),
        ("MES008", "Patricia García", "3201112300", "patricia.garcia@restaurante.com", 1),
        ("MES009", "Miguel Castro", "3201112311", "miguel.castro@restaurante.com", 8),
        ("MES010", "Laura Ramírez", "3201112322", "laura.ramirez@restaurante.com", 8),
        ("MES011", "Fernando Ruiz", "3201112333", "fernando.ruiz@restaurante.com", 2),
        ("MES012", "Elena Vargas", "3201112344", "elena.vargas@restaurante.com", 2),
        ("MES013", "Javier Soto", "3201112355", "javier.soto@restaurante.com", 5),
        ("MES014", "Gabriela Mendoza", "3201112366", "gabriela.mendoza@restaurante.com", 5),
        ("MES015", "Ricardo Flores", "3201112377", "ricardo.flores@restaurante.com", 8),
        ("MES016", "Verónica Bravo", "3201112388", "veronica.bravo@restaurante.com", 8),
        ("MES017", "Alejandro Nuñez", "3201112399", "alejandro.nunez@restaurante.com", 1),
        ("MES018", "Camila Espinoza", "3201112400", "camila.espinoza@restaurante.com", 2),
        ("MES019", "Diego Herrera", "3201112411", "diego.herrera@restaurante.com", 5),
        ("MES020", "Valentina Parra", "3201112422", "valentina.parra@restaurante.com", 8),
        ("MES021", "Francisco Vega", "3201112433", "francisco.vega@restaurante.com", 2),
        ("MES022", "Adriana Silva", "3201112444", "adriana.silva@restaurante.com", 5),
        ("MES023", "Gustavo Mora", "3201112455", "gustavo.mora@restaurante.com", 8),
        ("MES024", "Marcela Navarro", "3201112466", "marcela.navarro@restaurante.com", 1),
        ("MES025", "Sergio Romero", "3201112477", "sergio.romero@restaurante.com", 2),
        ("MES026", "Daniela Rojas", "3201112488", "daniela.rojas@restaurante.com", 5),
        ("MES027", "Mateo Durán", "3201112499", "mateo.duran@restaurante.com", 8),
        ("MES028", "Paula Araya", "3201112500", "paula.araya@restaurante.com", 1),
        ("MES029", "Nicolás Salazar", "3201112511", "nicolas.salazar@restaurante.com", 2),
        ("MES030", "Magdalena Vásquez", "3201112522", "magdalena.vasquez@restaurante.com", 5),
        ("MES031", "Enrique Molina", "3201112533", "enrique.molina@restaurante.com", 8),
        ("MES032", "Antonia Valenzuela", "3201112544", "antonia.valenzuela@restaurante.com", 1),
        ("MES033", "Tomás Sepúlveda", "3201112555", "tomas.sepulveda@restaurante.com", 2),
        ("MES034", "Constanza Fuentes", "3201112566", "constanza.fuentes@restaurante.com", 5),
        ("MES035", "Ignacio Ponce", "3201112577", "ignacio.ponce@restaurante.com", 8),
        ("MES036", "Beatriz Zamora", "3201112588", "beatriz.zamora@restaurante.com", 1),
        ("MES037", "Rodrigo Acuña", "3201112599", "rodrigo.acuna@restaurante.com", 2),
        ("MES038", "Francisca Muñoz", "3201112600", "francisca.munoz@restaurante.com", 5),
        ("MES039", "Patricio Donoso", "3201112611", "patricio.donoso@restaurante.com", 8),
        ("MES040", "Rosario Díaz", "3201112622", "rosario.diaz@restaurante.com", 1),
    ]
    
    print("Insertando 40 meseros...")
    for codigo, nombre, telefono, correo, id_jefe in meseros:
        insertar_mesero(conn, codigo, nombre, telefono, correo, id_jefe)
    
    # 7. RESERVAS (40)
    reservas = [
        (1, 1, 1, "2025-11-18", "RES001", "confirmada"),
        (2, 2, 1, "2025-11-18", "RES002", "confirmada"),
        (3, 3, 1, "2025-11-18", "RES003", "cancelada"),
        (4, 4, 2, "2025-11-18", "RES004", "confirmada"),
        (5, 5, 2, "2025-11-18", "RES005", "pendiente"),
        (6, 6, 3, "2025-11-18", "RES006", "confirmada"),
        (7, 7, 3, "2025-11-18", "RES007", "confirmada"),
        (8, 8, 4, "2025-11-19", "RES008", "pendiente"),
        (9, 9, 4, "2025-11-19", "RES009", "confirmada"),
        (10, 10, 5, "2025-11-19", "RES010", "confirmada"),
        (11, 1, 5, "2025-11-19", "RES011", "confirmada"),
        (12, 2, 6, "2025-11-19", "RES012", "cancelada"),
        (13, 3, 6, "2025-11-19", "RES013", "confirmada"),
        (14, 4, 7, "2025-11-20", "RES014", "pendiente"),
        (15, 5, 7, "2025-11-20", "RES015", "confirmada"),
        (16, 6, 8, "2025-11-20", "RES016", "confirmada"),
        (17, 7, 8, "2025-11-20", "RES017", "confirmada"),
        (18, 8, 9, "2025-11-20", "RES018", "pendiente"),
        (19, 9, 9, "2025-11-21", "RES019", "confirmada"),
        (20, 10, 10, "2025-11-21", "RES020", "confirmada"),
        (21, 1, 11, "2025-11-21", "RES021", "confirmada"),
        (22, 2, 11, "2025-11-21", "RES022", "pendiente"),
        (23, 3, 12, "2025-11-22", "RES023", "confirmada"),
        (24, 4, 12, "2025-11-22", "RES024", "confirmada"),
        (25, 5, 13, "2025-11-22", "RES025", "cancelada"),
        (26, 6, 13, "2025-11-22", "RES026", "confirmada"),
        (27, 7, 14, "2025-11-23", "RES027", "confirmada"),
        (28, 8, 14, "2025-11-23", "RES028", "pendiente"),
        (29, 9, 15, "2025-11-23", "RES029", "confirmada"),
        (30, 10, 15, "2025-11-23", "RES030", "confirmada"),
        (31, 1, 16, "2025-11-24", "RES031", "confirmada"),
        (32, 2, 16, "2025-11-24", "RES032", "pendiente"),
        (33, 3, 17, "2025-11-24", "RES033", "confirmada"),
        (34, 4, 17, "2025-11-24", "RES034", "confirmada"),
        (35, 5, 18, "2025-11-25", "RES035", "cancelada"),
        (36, 6, 18, "2025-11-25", "RES036", "confirmada"),
        (37, 7, 19, "2025-11-25", "RES037", "confirmada"),
        (38, 8, 19, "2025-11-25", "RES038", "pendiente"),
        (39, 9, 20, "2025-11-26", "RES039", "confirmada"),
        (40, 10, 20, "2025-11-26", "RES040", "confirmada"),
    ]
    
    print("Insertando 40 reservas...")
    for id_cliente, id_mesa, id_turno, fecha, codigo, estado in reservas:
        insertar_reserva(conn, id_cliente, id_mesa, id_turno, fecha, codigo, estado)
    
    # 8. PEDIDOS (40)
    pedidos = [
        (1, "PED001", "2025-11-18", "completado", 1),
        (2, "PED002", "2025-11-18", "completado", 2),
        (4, "PED003", "2025-11-18", "completado", 3),
        (6, "PED004", "2025-11-18", "en proceso", 4),
        (7, "PED005", "2025-11-18", "completado", 5),
        (9, "PED006", "2025-11-19", "en proceso", 6),
        (10, "PED007", "2025-11-19", "completado", 7),
        (11, "PED008", "2025-11-19", "completado", 1),
        (13, "PED009", "2025-11-19", "en proceso", 2),
        (15, "PED010", "2025-11-20", "completado", 3),
        (16, "PED011", "2025-11-20", "completado", 4),
        (17, "PED012", "2025-11-20", "en proceso", 5),
        (19, "PED013", "2025-11-21", "completado", 6),
        (20, "PED014", "2025-11-21", "en proceso", 7),
        (21, "PED015", "2025-11-21", "completado", 8),
        (23, "PED016", "2025-11-22", "completado", 9),
        (24, "PED017", "2025-11-22", "en proceso", 10),
        (26, "PED018", "2025-11-22", "completado", 1),
        (27, "PED019", "2025-11-23", "completado", 2),
        (29, "PED020", "2025-11-23", "en proceso", 3),
        (30, "PED021", "2025-11-23", "completado", 4),
        (31, "PED022", "2025-11-24", "completado", 5),
        (33, "PED023", "2025-11-24", "en proceso", 6),
        (34, "PED024", "2025-11-24", "completado", 7),
        (36, "PED025", "2025-11-25", "completado", 8),
        (37, "PED026", "2025-11-25", "en proceso", 9),
        (39, "PED027", "2025-11-25", "completado", 10),
        (40, "PED028", "2025-11-26", "completado", 1),
        (1, "PED029", "2025-11-26", "en proceso", 2),
        (3, "PED030", "2025-11-26", "completado", 3),
        (5, "PED031", "2025-11-26", "completado", 4),
        (8, "PED032", "2025-11-27", "en proceso", 5),
        (12, "PED033", "2025-11-27", "completado", 6),
        (14, "PED034", "2025-11-27", "completado", 7),
        (18, "PED035", "2025-11-28", "en proceso", 8),
        (22, "PED036", "2025-11-28", "completado", 9),
        (25, "PED037", "2025-11-28", "completado", 10),
        (28, "PED038", "2025-11-29", "en proceso", 1),
        (32, "PED039", "2025-11-29", "completado", 2),
        (35, "PED040", "2025-11-29", "completado", 3),
    ]
    
    print("Insertando 40 pedidos...")
    for id_reserva, codigo, fecha, estado, id_mesero in pedidos:
        insertar_pedido(conn, id_reserva, codigo, fecha, estado, id_mesero)
    
    # 9. DETALLE PEDIDOS (40)
    detalles = [
        (1, 1, "DET001", 2, 15.99),
        (1, 5, "DET002", 1, 9.99),
        (2, 3, "DET003", 1, 12.90),
        (2, 11, "DET004", 2, 5.20),
        (3, 7, "DET005", 1, 19.99),
        (4, 9, "DET006", 2, 13.40),
        (5, 2, "DET007", 1, 18.50),
        (6, 4, "DET008", 3, 11.50),
        (6, 6, "DET009", 2, 7.50),
        (7, 8, "DET010", 1, 10.50),
        (8, 10, "DET011", 2, 9.70),
        (9, 12, "DET012", 1, 6.80),
        (10, 13, "DET013", 3, 4.50),
        (11, 14, "DET014", 2, 8.20),
        (11, 16, "DET015", 1, 5.60),
        (12, 18, "DET016", 2, 13.80),
        (13, 20, "DET017", 1, 9.30),
        (14, 21, "DET018", 2, 16.90),
        (14, 22, "DET019", 1, 7.40),
        (15, 24, "DET020", 2, 10.90),
        (16, 25, "DET021", 1, 14.99),
        (17, 26, "DET022", 2, 9.80),
        (18, 27, "DET023", 1, 4.90),
        (19, 28, "DET024", 2, 16.20),
        (20, 29, "DET025", 1, 13.50),
        (21, 30, "DET026", 3, 7.80),
        (22, 31, "DET027", 2, 6.40),
        (23, 32, "DET028", 1, 3.50),
        (24, 33, "DET029", 2, 6.60),
        (25, 34, "DET030", 1, 5.00),
        (26, 35, "DET031", 2, 9.60),
        (27, 36, "DET032", 1, 12.40),
        (28, 37, "DET033", 2, 18.80),
        (29, 38, "DET034", 1, 15.10),
        (30, 39, "DET035", 3, 7.90),
        (31, 40, "DET036", 2, 13.20),
        (32, 1, "DET037", 1, 15.99),
        (33, 2, "DET038", 2, 18.50),
        (34, 3, "DET039", 1, 12.90),
        (35, 4, "DET040", 2, 11.50),
    ]
    
    print("Insertando 40 detalles de pedidos...")
    for id_pedido, id_plato, codigo, cantidad, precio_unitario in detalles:
        insertar_detalle_pedido(conn, id_pedido, id_plato, codigo, cantidad, precio_unitario)
    
    # 10. PAGOS (40)
    pagos = [
        ("PAG001", 1, "2025-11-18", 41.97, "Efectivo"),
        ("PAG002", 2, "2025-11-18", 32.10, "Tarjeta"),
        ("PAG003", 3, "2025-11-18", 19.99, "Tarjeta"),
        ("PAG004", 4, "2025-11-18", 40.80, "Efectivo"),
        ("PAG005", 5, "2025-11-18", 18.50, "Tarjeta"),
        ("PAG006", 6, "2025-11-19", 45.40, "Efectivo"),
        ("PAG007", 7, "2025-11-19", 19.40, "Tarjeta"),
        ("PAG008", 8, "2025-11-19", 27.50, "Tarjeta"),
        ("PAG009", 9, "2025-11-19", 10.80, "Efectivo"),
        ("PAG010", 10, "2025-11-20", 19.40, "Tarjeta"),
        ("PAG011", 11, "2025-11-20", 21.40, "Efectivo"),
        ("PAG012", 12, "2025-11-20", 31.60, "Tarjeta"),
        ("PAG013", 13, "2025-11-21", 13.50, "Efectivo"),
        ("PAG014", 14, "2025-11-21", 40.00, "Tarjeta"),
        ("PAG015", 15, "2025-11-21", 22.50, "Efectivo"),
        ("PAG016", 16, "2025-11-21", 29.80, "Tarjeta"),
        ("PAG017", 17, "2025-11-21", 18.60, "Efectivo"),
        ("PAG018", 18, "2025-11-22", 33.10, "Tarjeta"),
        ("PAG019", 19, "2025-11-22", 26.00, "Efectivo"),
        ("PAG020", 20, "2025-11-22", 20.80, "Tarjeta"),
        ("PAG021", 21, "2025-11-22", 37.80, "Efectivo"),
        ("PAG022", 22, "2025-11-23", 10.40, "Tarjeta"),
        ("PAG023", 23, "2025-11-23", 35.20, "Efectivo"),
        ("PAG024", 24, "2025-11-23", 29.70, "Tarjeta"),
        ("PAG025", 25, "2025-11-23", 15.90, "Efectivo"),
        ("PAG026", 26, "2025-11-24", 38.40, "Tarjeta"),
        ("PAG027", 27, "2025-11-24", 22.50, "Efectivo"),
        ("PAG028", 28, "2025-11-24", 48.60, "Tarjeta"),
        ("PAG029", 29, "2025-11-25", 27.00, "Efectivo"),
        ("PAG030", 30, "2025-11-25", 23.40, "Tarjeta"),
        ("PAG031", 31, "2025-11-25", 39.20, "Efectivo"),
        ("PAG032", 32, "2025-11-26", 24.80, "Tarjeta"),
        ("PAG033", 33, "2025-11-26", 37.60, "Efectivo"),
        ("PAG034", 34, "2025-11-26", 25.80, "Tarjeta"),
        ("PAG035", 35, "2025-11-26", 23.70, "Efectivo"),
        ("PAG036", 36, "2025-11-27", 18.40, "Tarjeta"),
        ("PAG037", 37, "2025-11-27", 31.98, "Efectivo"),
        ("PAG038", 38, "2025-11-27", 30.20, "Tarjeta"),
        ("PAG039", 39, "2025-11-28", 25.80, "Efectivo"),
        ("PAG040", 40, "2025-11-28", 22.10, "Tarjeta"),
    ]
    
    print("Insertando 40 pagos...")
    for codigo, id_pedido, fecha, monto, metodo in pagos:
        insertar_pago(conn, codigo, id_pedido, fecha, monto, metodo)
    
    # 11. MESERO_PEDIDO (40)
    mesero_pedidos = [
        (1, 1, "Mesero Principal"),
        (2, 2, "Asistente"),
        (3, 3, "Mesero Principal"),
        (4, 4, "Asistente"),
        (5, 5, "Mesero Principal"),
        (6, 6, "Asistente"),
        (7, 7, "Mesero Principal"),
        (8, 8, "Asistente"),
        (9, 9, "Mesero Principal"),
        (10, 10, "Asistente"),
        (11, 11, "Mesero Principal"),
        (12, 12, "Asistente"),
        (13, 13, "Mesero Principal"),
        (14, 14, "Asistente"),
        (15, 15, "Mesero Principal"),
        (16, 16, "Asistente"),
        (17, 17, "Mesero Principal"),
        (18, 18, "Asistente"),
        (19, 19, "Mesero Principal"),
        (20, 20, "Asistente"),
        (21, 21, "Mesero Principal"),
        (22, 22, "Asistente"),
        (23, 23, "Mesero Principal"),
        (24, 24, "Asistente"),
        (25, 25, "Mesero Principal"),
        (26, 26, "Asistente"),
        (27, 27, "Mesero Principal"),
        (28, 28, "Asistente"),
        (29, 29, "Mesero Principal"),
        (30, 30, "Asistente"),
        (31, 31, "Mesero Principal"),
        (32, 32, "Asistente"),
        (33, 33, "Mesero Principal"),
        (34, 34, "Asistente"),
        (35, 35, "Mesero Principal"),
        (36, 36, "Asistente"),
        (37, 37, "Mesero Principal"),
        (38, 38, "Asistente"),
        (39, 39, "Mesero Principal"),
        (40, 40, "Asistente"),
    ]
    
    print("Insertando 40 asignaciones mesero-pedido...")
    for id_mesero, id_pedido, rol in mesero_pedidos:
        insertar_mesero_pedido(conn, id_mesero, id_pedido, rol)
    
    conn.close()
    print("\n✅ ¡Inserciones completadas: 40 registros en cada tabla!")

if __name__ == "__main__":
    crear_todas_las_tablas()
    insertar_datos_completos()