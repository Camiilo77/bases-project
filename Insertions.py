#insercciones 

from mysql.connector import Error, IntegrityError

from Tables import conectar_bd 

connection = conectar_bd()
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

def insertar_mesero_pedido(connection, id_mesero, id_pedido, rol):  
    try:
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO MeseroPedido (id_mesero, id_pedido, rol)
               VALUES (%s, %s, %s)""",
            (id_mesero, id_pedido, rol)
        )
        connection.commit()
        print(f"MeseroPedido con mesero ID '{id_mesero}' y pedido ID '{id_pedido}' insertado exitosamente")
    except IntegrityError:
        print(f"La relación entre mesero ID '{id_mesero}' y pedido ID '{id_pedido}' ya existe")
    except Error as err:
        print(f"Error al insertar MeseroPedido: {err}") 

if __name__ == "__main__":
    conectar_bd()
    insertar_categoria_plato(connection, 'mojarra frita', 'CAT001' )
    insertar_categoria_plato(connection, 'Caviar', 'CAT002' )
    insertar_categoria_plato(connection, 'Clamar', 'CAT003' )
    insertar_categoria_plato(connection, 'Arroz marinado', 'CAT004')
    insertar_categoria_plato(connection, 'Arroz marinado', 'CAT004')
    insertar_categoria_plato(connection, 'Carnes a la parrilla', 'CAT005')
    insertar_categoria_plato(connection, 'Pastas frescas', 'CAT006')
    insertar_categoria_plato(connection, 'Ensaladas verdes', 'CAT007')
    insertar_categoria_plato(connection, 'Sopas tradicionales', 'CAT008')
    insertar_categoria_plato(connection, 'Mariscos especiales', 'CAT009')
    insertar_categoria_plato(connection, 'Comidas rápidas', 'CAT010')
    insertar_categoria_plato(connection, 'Desayunos típicos', 'CAT011')
    insertar_categoria_plato(connection, 'Jugos naturales', 'CAT012')
    insertar_categoria_plato(connection, 'Bebidas calientes', 'CAT013')
    insertar_categoria_plato(connection, 'Postres artesanales', 'CAT014')
    insertar_categoria_plato(connection, 'Snacks y entradas', 'CAT015')
    insertar_categoria_plato(connection, 'Platos vegetarianos', 'CAT016')
    insertar_categoria_plato(connection, 'Platos veganos', 'CAT017')
    insertar_categoria_plato(connection, 'Comidas internacionales', 'CAT018')
    insertar_categoria_plato(connection, 'Pollos especiales', 'CAT019')
    insertar_categoria_plato(connection, 'Arroces orientales', 'CAT020')
    insertar_categoria_plato(connection, 'Hamburguesas premium', 'CAT021')
    insertar_categoria_plato(connection, 'Bebidas gaseosas', 'CAT022')
    insertar_categoria_plato(connection, 'Cocteles especiales', 'CAT023')
    insertar_categoria_plato(connection, 'Tostadas gourmet', 'CAT024')
    insertar_categoria_plato(connection, 'Cremas y caldos', 'CAT025')
    insertar_categoria_plato(connection, 'Pescados al horno', 'CAT026')
    insertar_categoria_plato(connection, 'Platos al vapor', 'CAT027')
    insertar_categoria_plato(connection, 'Helados artesanales', 'CAT028')
    insertar_categoria_plato(connection, 'Platos mexicanos', 'CAT029')
    insertar_categoria_plato(connection, 'Platos italianos', 'CAT030')
    insertar_categoria_plato(connection, 'Platos japoneses', 'CAT031')
    insertar_categoria_plato(connection, 'Comida china', 'CAT032')
    insertar_categoria_plato(connection, 'Cafés especiales', 'CAT033')
    insertar_categoria_plato(connection, 'Panadería artesanal', 'CAT034')
    insertar_categoria_plato(connection, 'Platos sin gluten', 'CAT035')
    insertar_categoria_plato(connection, 'Platos sin azúcar', 'CAT036')
    insertar_categoria_plato(connection, 'Bebidas energéticas', 'CAT037')
    insertar_categoria_plato(connection, 'Tés e infusiones', 'CAT038')
    insertar_categoria_plato(connection, 'Sándwiches artesanales', 'CAT039')
    insertar_categoria_plato(connection, 'Arepas especiales', 'CAT040')
    insertar_categoria_plato(connection, 'Comida árabe', 'CAT041')
    insertar_categoria_plato(connection, 'Platos fusion', 'CAT042')
    insertar_categoria_plato(connection, 'Brochetas y pinchos', 'CAT043')


    insertar_plato(connection, 'camarones al agillo', 'PLT001', 'Camarones frescos salteados en aceite de oliva con ajo y perejil', 15.99, 1)
    insertar_plato(connection, 'Camarones al ajillo', 'PLT001', 'Camarones frescos salteados en aceite de oliva con ajo y perejil', 15.99, 1)
    insertar_plato(connection, 'Arroz con mariscos', 'PLT002', 'Arroz cremoso con mezcla de mariscos frescos', 18.50, 1)
    insertar_plato(connection, 'Pasta alfredo', 'PLT003', 'Fettuccine en salsa cremosa de queso parmesano', 12.90, 2)
    insertar_plato(connection, 'Pollo a la plancha', 'PLT004', 'Pechuga de pollo jugosa con especias caseras', 11.50, 3)
    insertar_plato(connection, 'Ensalada césar', 'PLT005', 'Lechuga, crotones, queso parmesano y aderezo césar', 9.99, 4)
    insertar_plato(connection, 'Sopa de tomate', 'PLT006', 'Sopa cremosa de tomate con especias italianas', 7.50, 5)
    insertar_plato(connection, 'Filete de salmón', 'PLT007', 'Salmón al horno con limón y eneldo', 19.99, 6)
    insertar_plato(connection, 'Hamburguesa clásica', 'PLT008', 'Carne 100% angus con queso y vegetales frescos', 10.50, 7)
    insertar_plato(connection, 'Pizza margarita', 'PLT009', 'Pizza artesanal con mozzarella y albahaca', 13.40, 8)
    insertar_plato(connection, 'Tacos mexicanos', 'PLT010', 'Tortillas rellenas con carne marinada y vegetales', 9.70, 9)
    insertar_plato(connection, 'Batido de mango', 'PLT011', 'Batido natural preparado con mango fresco', 5.20, 10)
    insertar_plato(connection, 'Café latte', 'PLT012', 'Café espresso con leche espumada', 3.90, 11)
    insertar_plato(connection, 'Cheesecake de fresa', 'PLT013', 'Postre cremoso con salsa de fresa natural', 6.80, 12)
    insertar_plato(connection, 'Empanadas caseras', 'PLT014', 'Empanadas fritas rellenas de carne o pollo', 4.50, 13)
    insertar_plato(connection, 'Wrap de pollo', 'PLT015', 'Tortilla rellena de pollo asado y vegetales', 8.20, 14)
    insertar_plato(connection, 'Lomo saltado', 'PLT016', 'Carne salteada con cebolla, tomate y papas', 14.30, 15)
    insertar_plato(connection, 'Arepa rellena', 'PLT017', 'Arepa rellena con queso y jamón', 5.60, 16)
    insertar_plato(connection, 'Sushi mixto', 'PLT018', 'Rollos de sushi con salmón, camarón y cangrejo', 17.20, 17)
    insertar_plato(connection, 'Ramen japonés', 'PLT019', 'Caldo tradicional japonés con fideos y toppings', 13.80, 17)
    insertar_plato(connection, 'Arroz frito oriental', 'PLT020', 'Arroz salteado con vegetales y salsa de soya', 9.30, 18)
    insertar_plato(connection, 'Costillas BBQ', 'PLT021', 'Costillas de cerdo bañadas en salsa BBQ', 16.90, 19)
    insertar_plato(connection, 'Papas gratinadas', 'PLT022', 'Papas horneadas con crema y queso fundido', 7.40, 20)
    insertar_plato(connection, 'Tostadas francesas', 'PLT023', 'Pan dulce bañado en huevo y canela', 8.10, 21)
    insertar_plato(connection, 'Bowl vegano', 'PLT024', 'Mezcla de quinoa, tofu y vegetales frescos', 10.90, 22)
    insertar_plato(connection, 'Canelones rellenos', 'PLT025', 'Pasta rellena de carne con salsa bechamel', 14.99, 23)
    insertar_plato(connection, 'Sándwich premium', 'PLT026', 'Pan artesanal con jamón, queso y vegetales', 9.80, 24)
    insertar_plato(connection, 'Helado artesanal', 'PLT027', 'Helado preparado con frutas naturales', 4.90, 25)
    insertar_plato(connection, 'Camarones empanizados', 'PLT028', 'Camarones crujientes acompañados de salsa tártara', 16.20, 1)
    insertar_plato(connection, 'Pechuga rellena', 'PLT029', 'Pollo relleno de queso y espinaca', 13.50, 3)
    insertar_plato(connection, 'Crema de champiñones', 'PLT030', 'Crema suave de champiñones frescos', 7.80, 5)
    insertar_plato(connection, 'Nuggets caseros', 'PLT031', 'Nuggets de pollo empanizados artesanalmente', 6.40, 7)
    insertar_plato(connection, 'Té chai', 'PLT032', 'Infusión de especias con leche', 3.50, 11)
    insertar_plato(connection, 'Brownie con helado', 'PLT033', 'Brownie caliente con bola de helado', 6.60, 12)
    insertar_plato(connection, 'Bebida de maracuyá', 'PLT034', 'Jugo natural de maracuyá sin azúcar añadida', 5.00, 10)
    insertar_plato(connection, 'Panini italiano', 'PLT035', 'Pan tostado con pepperoni y queso mozzarella', 9.60, 24)
    insertar_plato(connection, 'Pasta boloñesa', 'PLT036', 'Espaguetis con salsa de carne tradicional', 12.40, 2)
    insertar_plato(connection, 'Churrasco premium', 'PLT037', 'Corte de carne jugoso asado a la parrilla', 18.80, 19)
    insertar_plato(connection, 'Ceviche peruano', 'PLT038', 'Pescado fresco marinado en limón con cebolla', 15.10, 6)
    insertar_plato(connection, 'Waffles con miel', 'PLT039', 'Waffles suaves con miel y frutas', 7.90, 21)
    insertar_plato(connection, 'Pollo teriyaki', 'PLT040', 'Pollo salteado con salsa teriyaki y vegetales', 13.20, 18)

    insertar_mesa(connection, 'MESA01', 4)
    insertar_mesa(connection, 'MESA01', 20)
    insertar_mesa(connection, 'MESA01', 2)
    insertar_mesa(connection, 'MESA01', 5)
    insertar_mesa(connection, 'MESA01', 25)
    insertar_mesa(connection, 'MESA01', 8)
    insertar_mesa(connection, 'MESA01', 4)
    insertar_mesa(connection, 'MESA01', 4)
    insertar_mesa(connection, 'MESA01', 2)
    insertar_mesa(connection, 'MESA01', 4)
    insertar_mesa(connection, 'MESA01', 8)
    insertar_mesa(connection, 'MESA01', 8)
    insertar_mesa(connection, 'MESA01', 20)
    insertar_mesa(connection, 'MESA01', 8)
    insertar_mesa(connection, 'MESA01', 10)
    insertar_mesa(connection, 'MESA01', 10)
    insertar_mesa(connection, 'MESA01', 2)
    insertar_mesa(connection, 'MESA01', 2)
    insertar_mesa(connection, 'MESA01', 4)
    insertar_mesa(connection, 'MESA01', 5)
    insertar_mesa(connection, 'MESA01', 15)
    insertar_mesa(connection, 'MESA01', 2)
    insertar_mesa(connection, 'MESA01', 2)
    insertar_mesa(connection, 'MESA01', 2)
    insertar_mesa(connection, 'MESA01', 5)
    insertar_mesa(connection, 'MESA01', 5)
    insertar_mesa(connection, 'MESA01', 5)
    insertar_mesa(connection, 'MESA01', 3)
    insertar_mesa(connection, 'MESA01', 4)
    insertar_mesa(connection, 'MESA01', 15)
    insertar_mesa(connection, 'MESA01', 3)
    insertar_mesa(connection, 'MESA01', 9)
    insertar_mesa(connection, 'MESA01', 4)
    insertar_mesa(connection, 'MESA01', 15)
    insertar_mesa(connection, 'MESA01', 2)
    insertar_mesa(connection, 'MESA01', 2)
    insertar_mesa(connection, 'MESA01', 8)
    insertar_mesa(connection, 'MESA01', 5)
    insertar_mesa(connection, 'MESA01', 14)
    insertar_mesa(connection, 'MESA01', 7)


    insertar_cliente(connection, 'CL01', 'Juan Perez', '555-1234', 'juanperez@gmail')
    insertar_cliente(connection, 'CL02', 'Ivan Petrov', '555-1001', 'ivan.petrov@mail.ru')
insertar_cliente(connection, 'CL03', 'Sergey Ivanov', '555-1002', 'sergey.ivanov@mail.ru')
insertar_cliente(connection, 'CL04', 'Dmitri Volkov', '555-1003', 'dmitri.volkov@mail.ru')
insertar_cliente(connection, 'CL05', 'Alexei Smirnov', '555-1004', 'alexei.smirnov@mail.ru')
insertar_cliente(connection, 'CL06', 'Mikhail Orlov', '555-1005', 'mikhail.orlov@mail.ru')
insertar_cliente(connection, 'CL07', 'Nikolai Pavlov', '555-1006', 'nikolai.pavlov@mail.ru')
insertar_cliente(connection, 'CL08', 'Yuri Sokolov', '555-1007', 'yuri.sokolov@mail.ru')
insertar_cliente(connection, 'CL09', 'Vladimir Kuznetsov', '555-1008', 'vladimir.kuznetsov@mail.ru')
insertar_cliente(connection, 'CL10', 'Oleg Morozov', '555-1009', 'oleg.morozov@mail.ru')
insertar_cliente(connection, 'CL11', 'Roman Egorov', '555-1010', 'roman.egorov@mail.ru')
insertar_cliente(connection, 'CL12', 'Anastasia Petrova', '555-1011', 'anastasia.petrova@mail.ru')
insertar_cliente(connection, 'CL13', 'Elena Smirnova', '555-1012', 'elena.smirnova@mail.ru')
insertar_cliente(connection, 'CL14', 'Irina Popova', '555-1013', 'irina.popova@mail.ru')
insertar_cliente(connection, 'CL15', 'Natalia Volkova', '555-1014', 'natalia.volkova@mail.ru')
insertar_cliente(connection, 'CL16', 'Tatiana Orlova', '555-1015', 'tatiana.orlova@mail.ru')
insertar_cliente(connection, 'CL17', 'Olga Pavlova', '555-1016', 'olga.pavlova@mail.ru')
insertar_cliente(connection, 'CL18', 'Svetlana Sokolova', '555-1017', 'svetlana.sokolova@mail.ru')
insertar_cliente(connection, 'CL19', 'Marina Kuznetsova', '555-1018', 'marina.kuznetsova@mail.ru')
insertar_cliente(connection, 'CL20', 'Ekaterina Morozova', '555-1019', 'ekaterina.morozova@mail.ru')
insertar_cliente(connection, 'CL21', 'Polina Egorova', '555-1020', 'polina.egorova@mail.ru')
insertar_cliente(connection, 'CL22', 'Oleksandr Shevchenko', '555-1021', 'oleksandr.shevchenko@ukr.net')
insertar_cliente(connection, 'CL23', 'Andriy Kovalenko', '555-1022', 'andriy.kovalenko@ukr.net')
insertar_cliente(connection, 'CL24', 'Danylo Bondarenko', '555-1023', 'danylo.bondarenko@ukr.net')
insertar_cliente(connection, 'CL25', 'Mykola Melnyk', '555-1024', 'mykola.melnyk@ukr.net')
insertar_cliente(connection, 'CL26', 'Petro Tkachenko', '555-1025', 'petro.tkachenko@ukr.net')
insertar_cliente(connection, 'CL27', 'Volodymyr Kravchenko', '555-1026', 'volodymyr.kravchenko@ukr.net')
insertar_cliente(connection, 'CL28', 'Yaroslav Polishchuk', '555-1027', 'yaroslav.polishchuk@ukr.net')
insertar_cliente(connection, 'CL29', 'Serhiy Lysenko', '555-1028', 'serhiy.lysenko@ukr.net')
insertar_cliente(connection, 'CL30', 'Vasyl Horbenko', '555-1029', 'vasyl.horbenko@ukr.net')
insertar_cliente(connection, 'CL31', 'Ihor Dovzhenko', '555-1030', 'ihor.dovzhenko@ukr.net')
insertar_cliente(connection, 'CL32', 'Oksana Shevchenko', '555-1031', 'oksana.shevchenko@ukr.net')
insertar_cliente(connection, 'CL33', 'Kateryna Kovalenko', '555-1032', 'kateryna.kovalenko@ukr.net')
insertar_cliente(connection, 'CL34', 'Iryna Bondarenko', '555-1033', 'iryna.bondarenko@ukr.net')
insertar_cliente(connection, 'CL35', 'Tetiana Melnyk', '555-1034', 'tetiana.melnyk@ukr.net')
insertar_cliente(connection, 'CL36', 'Nadiya Tkachenko', '555-1035', 'nadiya.tkachenko@ukr.net')
insertar_cliente(connection, 'CL37', 'Halyna Kravchenko', '555-1036', 'halyna.kravchenko@ukr.net')
insertar_cliente(connection, 'CL38', 'Liudmyla Polishchuk', '555-1037', 'liudmyla.polishchuk@ukr.net')
insertar_cliente(connection, 'CL39', 'Olena Lysenko', '555-1038', 'olena.lysenko@ukr.net')
insertar_cliente(connection, 'CL40', 'Sofiia Horbenko', '555-1039', 'sofiia.horbenko@ukr.net')
insertar_cliente(connection, 'CL41', 'Mariia Dovzhenko', '555-1040', 'mariia.dovzhenko@ukr.net')

insertar_turno(connection, 'TUR001', '2024-10-01', '09:00:00', '15:00:00')
insertar_turno(connection, 'TUR002', '2024-10-01', '15:00:00', '21:00:00')
insertar_turno(connection, 'TUR003', '2024-10-02', '09:00:00', '15:00:00')
insertar_turno(connection, 'TUR004', '2024-10-02', '15:00:00', '21:00:00')
insertar_turno(connection, 'TUR005', '2024-10-03', '09:00:00', '15:00:00')
insertar_turno(connection, 'TUR006', '2024-10-03', '15:00:00', '21:00:00')
insertar_turno(connection, 'TUR007', '2024-10-04', '09:00:00', '15:00:00')
insertar_turno(connection, 'TUR008', '2024-10-04', '15:00:00', '21:00:00')
insertar_turno(connection, 'TUR010', '2024-10-05', '15:00:00', '21:00:00')
insertar_turno(connection, 'TUR011', '2024-10-06', '09:00:00', '15:00:00')

insertar_turno(connection, 'TUR012', '2024-10-06', '15:00:00', '21:00:00')
insertar_turno(connection, 'TUR013', '2024-10-07', '09:00:00', '15:00:00')
insertar_turno(connection, 'TUR014', '2024-10-07', '15:00:00', '21:00:00')
insertar_turno(connection, 'TUR015', '2024-10-08', '09:00:00', '15:00:00')
insertar_turno(connection, 'TUR016', '2024-10-08', '15:00:00', '21:00:00')
insertar_turno(connection, 'TUR017', '2024-10-09', '09:00:00', '15:00:00')
insertar_turno(connection, 'TUR018', '2024-10-09', '15:00:00', '21:00:00')
insertar_turno(connection, 'TUR019', '2024-10-10', '09:00:00', '15:00:00')
insertar_turno(connection, 'TUR020', '2024-10-10', '15:00:00', '21:00:00')
insertar_turno(connection, 'TUR021', '2024-10-11', '09:00:00', '15:00:00')
insertar_turno(connection, 'TUR022', '2024-10-11', '21:00:00', '03:00:00')
insertar_turno(connection, 'TUR023', '2024-10-12', '21:00:00', '03:00:00')
insertar_turno(connection, 'TUR024', '2024-10-13', '21:00:00', '03:00:00')
insertar_turno(connection, 'TUR025', '2024-10-14', '21:00:00', '03:00:00')
insertar_turno(connection, 'TUR026', '2024-10-15', '21:00:00', '03:00:00')
insertar_turno(connection, 'TUR027', '2024-10-16', '21:00:00', '03:00:00')
insertar_turno(connection, 'TUR028', '2024-10-17', '21:00:00', '03:00:00')
insertar_turno(connection, 'TUR029', '2024-10-18', '21:00:00', '03:00:00')
insertar_turno(connection, 'TUR031', '2024-10-20', '21:00:00', '03:00:00')
insertar_turno(connection, 'TUR032', '2024-10-21', '03:00:00', '09:00:00')
insertar_turno(connection, 'TUR033', '2024-10-22', '03:00:00', '09:00:00')
insertar_turno(connection, 'TUR034', '2024-10-23', '03:00:00', '09:00:00')
insertar_turno(connection, 'TUR035', '2024-10-24', '03:00:00', '09:00:00')
insertar_turno(connection, 'TUR036', '2024-10-25', '03:00:00', '09:00:00')
insertar_turno(connection, 'TUR037', '2024-10-26', '03:00:00', '09:00:00')
insertar_turno(connection, 'TUR039', '2024-10-28', '03:00:00', '09:00:00')
insertar_turno(connection, 'TUR040', '2024-10-29', '03:00:00', '09:00:00')
insertar_turno(connection, 'TUR041', '2024-10-30', '03:00:00', '09:00:00')
