# consultas 
from Tables import conectar_bd

def ejecutar_query(conn, query, descripcion):
    """Función auxiliar para ejecutar y mostrar resultados"""
    print(f"\n{':p'*80}")
    print(f" {descripcion}")
    print(f"{':p'*80}")
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        
        if resultados:
            columnas = [i[0] for i in cursor.description]
            print(f"\n{' | '.join(columnas)}")
            print("-" * 80)
            
            for fila in resultados:
                print(f"{' | '.join(str(x) for x in fila)}")
            print(f"\nTotal de registros: {len(resultados)}")
        else:
            print("No hay resultados")
    except Exception as e:
        print(f"❌ Error: {e}")

# ... QUERIES ORIGINALES (1-15) ...
def query_1_ingresos_por_mesero(conn):
    query = """
    SELECT 
        m.codigo_mesero,
        m.nombre,
        COUNT(DISTINCT p.id_pedido) as total_pedidos,
        SUM(pa.monto) as ingresos_totales,
        ROUND(AVG(pa.monto), 2) as promedio_pedido
    FROM Mesero m
    LEFT JOIN Pedido p ON m.id_mesero = p.id_mesero
    LEFT JOIN Pago pa ON p.id_pedido = pa.id_pedido
    GROUP BY m.id_mesero, m.codigo_mesero, m.nombre
    ORDER BY ingresos_totales DESC
    LIMIT 20;
    """
    ejecutar_query(conn, query, "QUERY 1: Ingresos por Mesero")

def query_2_platos_mas_vendidos(conn):
    query = """
    SELECT 
        p.codigo_plato,
        p.nombre,
        c.nombre as categoria,
        SUM(dp.cantidad) as total_vendido,
        COUNT(DISTINCT dp.id_pedido) as num_pedidos,
        ROUND(AVG(dp.precio_unitario), 2) as precio_promedio,
        ROUND(SUM(dp.cantidad * dp.precio_unitario), 2) as ingresos_totales
    FROM Plato p
    INNER JOIN CategoriaPlato c ON p.id_categoria = c.id_categoria
    LEFT JOIN DetallePedido dp ON p.id_plato = dp.id_plato
    GROUP BY p.id_plato, p.codigo_plato, p.nombre, c.nombre
    ORDER BY total_vendido DESC
    LIMIT 15;
    """
    ejecutar_query(conn, query, "QUERY 2: Top 15 Platos Más Vendidos")

def query_3_ocupacion_mesas(conn):
    query = """
    SELECT 
        m.codigo_mesa,
        m.capacidad,
        COUNT(DISTINCT r.id_reserva) as num_reservas,
        ROUND(COUNT(DISTINCT r.id_reserva) / 40 * 100, 2) as porcentaje_uso,
        SUM(CASE WHEN r.estado = 'confirmada' THEN 1 ELSE 0 END) as confirmadas,
        SUM(CASE WHEN r.estado = 'cancelada' THEN 1 ELSE 0 END) as canceladas,
        SUM(CASE WHEN r.estado = 'pendiente' THEN 1 ELSE 0 END) as pendientes
    FROM Mesa m
    LEFT JOIN Reserva r ON m.id_mesa = r.id_mesa
    GROUP BY m.id_mesa, m.codigo_mesa, m.capacidad
    ORDER BY num_reservas DESC
    LIMIT 20;
    """
    ejecutar_query(conn, query, "QUERY 3: Ocupación de Mesas")

def query_4_clientes_frecuentes(conn):
    query = """
    SELECT 
        c.codigo_cliente,
        c.nombre,
        c.telefono,
        c.correo,
        COUNT(DISTINCT r.id_reserva) as num_reservas,
        COUNT(DISTINCT p.id_pedido) as num_pedidos,
        ROUND(SUM(pa.monto), 2) as gasto_total,
        ROUND(AVG(pa.monto), 2) as gasto_promedio,
        MAX(pa.fecha_pago) as ultima_visita
    FROM Cliente c
    LEFT JOIN Reserva r ON c.id_cliente = r.id_cliente
    LEFT JOIN Pedido p ON r.id_reserva = p.id_reserva
    LEFT JOIN Pago pa ON p.id_pedido = pa.id_pedido
    GROUP BY c.id_cliente, c.codigo_cliente, c.nombre, c.telefono, c.correo
    HAVING COUNT(DISTINCT r.id_reserva) > 0
    ORDER BY gasto_total DESC
    LIMIT 15;
    """
    ejecutar_query(conn, query, "QUERY 4: Clientes Más Frecuentes")

def query_5_categorias_mas_vendidas(conn):
    query = """
    SELECT 
        c.codigo_categoria,
        c.nombre as categoria,
        COUNT(DISTINCT p.id_plato) as num_platos,
        SUM(dp.cantidad) as total_items_vendidos,
        ROUND(SUM(dp.cantidad * dp.precio_unitario), 2) as ingresos_categoria,
        ROUND(AVG(dp.cantidad), 2) as promedio_items_pedido,
        COUNT(DISTINCT dp.id_pedido) as num_pedidos
    FROM CategoriaPlato c
    LEFT JOIN Plato p ON c.id_categoria = p.id_categoria
    LEFT JOIN DetallePedido dp ON p.id_plato = dp.id_plato
    GROUP BY c.id_categoria, c.codigo_categoria, c.nombre
    ORDER BY ingresos_categoria DESC;
    """
    ejecutar_query(conn, query, "QUERY 5: Categorías Más Vendidas")

def query_6_analisis_turnos(conn):
    query = """
    SELECT 
        t.codigo_turno,
        DATE(t.fecha) as fecha,
        TIME_FORMAT(t.hora_inicio, '%H:%i') as hora_inicio,
        TIME_FORMAT(t.hora_fin, '%H:%i') as hora_fin,
        COUNT(DISTINCT p.id_pedido) as num_pedidos,
        COUNT(DISTINCT r.id_reserva) as num_reservas,
        ROUND(SUM(pa.monto), 2) as ingresos,
        ROUND(AVG(pa.monto), 2) as promedio_pedido
    FROM Turno t
    LEFT JOIN Reserva r ON t.id_turno = r.id_turno
    LEFT JOIN Pedido p ON r.id_reserva = p.id_reserva
    LEFT JOIN Pago pa ON p.id_pedido = pa.id_pedido
    GROUP BY t.id_turno, t.codigo_turno, DATE(t.fecha), t.hora_inicio, t.hora_fin
    ORDER BY t.fecha DESC, t.hora_inicio
    LIMIT 20;
    """
    ejecutar_query(conn, query, "QUERY 6: Análisis de Turnos")

def query_7_metodos_pago(conn):
    query = """
    SELECT 
        metodo,
        COUNT(*) as num_transacciones,
        ROUND(SUM(monto), 2) as monto_total,
        ROUND(AVG(monto), 2) as promedio_transaccion,
        ROUND(MIN(monto), 2) as monto_minimo,
        ROUND(MAX(monto), 2) as monto_maximo,
        ROUND(SUM(monto) / (SELECT SUM(monto) FROM Pago) * 100, 2) as porcentaje_total
    FROM Pago
    GROUP BY metodo
    ORDER BY monto_total DESC;
    """
    ejecutar_query(conn, query, "QUERY 7: Análisis de Métodos de Pago")

def query_8_estado_pedidos(conn):
    query = """
    SELECT 
        estado,
        COUNT(*) as cantidad,
        ROUND(COUNT(*) / (SELECT COUNT(*) FROM Pedido) * 100, 2) as porcentaje,
        ROUND(AVG(
            (SELECT SUM(dp.cantidad * dp.precio_unitario) 
             FROM DetallePedido dp 
             WHERE dp.id_pedido = Pedido.id_pedido)
        ), 2) as monto_promedio
    FROM Pedido
    GROUP BY estado
    ORDER BY cantidad DESC;
    """
    ejecutar_query(conn, query, "QUERY 8: Distribución de Estados de Pedidos")

def query_9_reservas_por_estado(conn):
    query = """
    SELECT 
        estado,
        COUNT(*) as total_reservas,
        ROUND(COUNT(*) / (SELECT COUNT(*) FROM Reserva) * 100, 2) as porcentaje,
        DATE(MIN(fecha_reserva)) as fecha_primera,
        DATE(MAX(fecha_reserva)) as fecha_ultima,
        COUNT(DISTINCT id_cliente) as clientes_unicos
    FROM Reserva
    GROUP BY estado
    ORDER BY total_reservas DESC;
    """
    ejecutar_query(conn, query, "QUERY 9: Análisis de Reservas por Estado")

def query_10_meseros_jerarquia(conn):
    query = """
    SELECT 
        m.id_mesero,
        m.codigo_mesero,
        m.nombre as mesero,
        COALESCE(jefe.nombre, 'SIN JEFE (Jefe Principal)') as jefe,
        COUNT(DISTINCT p.id_pedido) as pedidos_atendidos,
        ROUND(SUM(pa.monto), 2) as ingresos_generados
    FROM Mesero m
    LEFT JOIN Mesero jefe ON m.id_jefe = jefe.id_mesero
    LEFT JOIN Pedido p ON m.id_mesero = p.id_mesero
    LEFT JOIN Pago pa ON p.id_pedido = pa.id_pedido
    GROUP BY m.id_mesero, m.codigo_mesero, m.nombre, jefe.nombre
    ORDER BY jefe, m.nombre
    LIMIT 30;
    """
    ejecutar_query(conn, query, "QUERY 10: Estructura Jerárquica de Meseros")

def query_11_ingresos_diarios(conn):
    query = """
    SELECT 
        DATE(pa.fecha_pago) as fecha,
        COUNT(DISTINCT pa.id_pago) as num_transacciones,
        COUNT(DISTINCT p.id_pedido) as num_pedidos,
        ROUND(SUM(pa.monto), 2) as ingresos_diarios,
        ROUND(AVG(pa.monto), 2) as ticket_promedio,
        ROUND(MIN(pa.monto), 2) as venta_minima,
        ROUND(MAX(pa.monto), 2) as venta_maxima
    FROM Pago pa
    LEFT JOIN Pedido p ON pa.id_pedido = p.id_pedido
    GROUP BY DATE(pa.fecha_pago)
    ORDER BY fecha DESC;
    """
    ejecutar_query(conn, query, "QUERY 11: Ingresos Diarios")

def query_12_platos_por_pedido(conn):
    query = """
    SELECT 
        p.codigo_pedido,
        p.fecha_pedido,
        c.nombre as cliente,
        m.nombre as mesero,
        COUNT(DISTINCT dp.id_plato) as num_platos_diferentes,
        SUM(dp.cantidad) as cantidad_total_items,
        ROUND(SUM(dp.cantidad * dp.precio_unitario), 2) as total_pedido,
        p.estado
    FROM Pedido p
    INNER JOIN Reserva r ON p.id_reserva = r.id_reserva
    INNER JOIN Cliente c ON r.id_cliente = c.id_cliente
    INNER JOIN Mesero m ON p.id_mesero = m.id_mesero
    LEFT JOIN DetallePedido dp ON p.id_pedido = dp.id_pedido
    GROUP BY p.id_pedido, p.codigo_pedido, p.fecha_pedido, c.nombre, m.nombre, p.estado
    ORDER BY total_pedido DESC
    LIMIT 20;
    """
    ejecutar_query(conn, query, "QUERY 12: Detalles de Pedidos (Top 20)")

def query_13_capacidad_mesas_optimizacion(conn):
    query = """
    SELECT 
        CASE 
            WHEN m.capacidad <= 2 THEN 'Pequeña (2 personas)'
            WHEN m.capacidad <= 4 THEN 'Mediana (4 personas)'
            WHEN m.capacidad <= 6 THEN 'Grande (6 personas)'
            ELSE 'Muy Grande (8+ personas)'
        END as tipo_mesa,
        COUNT(DISTINCT m.id_mesa) as num_mesas,
        COUNT(DISTINCT r.id_reserva) as total_reservas,
        ROUND(AVG(m.capacidad), 0) as capacidad_promedio,
        SUM(CASE WHEN r.estado = 'confirmada' THEN 1 ELSE 0 END) as reservas_confirmadas,
        ROUND(SUM(CASE WHEN r.estado = 'confirmada' THEN 1 ELSE 0 END) / COUNT(DISTINCT r.id_reserva) * 100, 2) as tasa_confirmacion
    FROM Mesa m
    LEFT JOIN Reserva r ON m.id_mesa = r.id_mesa
    GROUP BY tipo_mesa
    ORDER BY capacidad_promedio;
    """
    ejecutar_query(conn, query, "QUERY 13: Optimización de Capacidad de Mesas")

def query_14_comparativa_turnos(conn):
    query = """
    SELECT 
        CASE 
            WHEN HOUR(t.hora_inicio) < 12 THEN 'MAÑANA'
            WHEN HOUR(t.hora_inicio) < 18 THEN 'TARDE'
            ELSE 'NOCHE'
        END as turno,
        COUNT(DISTINCT r.id_reserva) as reservas,
        COUNT(DISTINCT p.id_pedido) as pedidos,
        ROUND(SUM(pa.monto), 2) as ingresos,
        ROUND(AVG(pa.monto), 2) as ticket_promedio,
        ROUND(SUM(pa.monto) / COUNT(DISTINCT r.id_reserva), 2) as ingreso_por_reserva,
        COUNT(DISTINCT m.id_mesa) as mesas_utilizadas
    FROM Turno t
    LEFT JOIN Reserva r ON t.id_turno = r.id_turno
    LEFT JOIN Pedido p ON r.id_reserva = p.id_reserva
    LEFT JOIN Pago pa ON p.id_pedido = pa.id_pedido
    LEFT JOIN Mesa m ON r.id_mesa = m.id_mesa
    GROUP BY turno
    ORDER BY ingresos DESC;
    """
    ejecutar_query(conn, query, "QUERY 14: Comparativa de Rendimiento entre Turnos")

def query_15_cancellations_analysis(conn):
    query = """
    SELECT 
        DATE(r.fecha_reserva) as fecha,
        COUNT(DISTINCT CASE WHEN r.estado = 'cancelada' THEN r.id_reserva END) as canceladas,
        COUNT(DISTINCT CASE WHEN r.estado = 'confirmada' THEN r.id_reserva END) as confirmadas,
        COUNT(DISTINCT CASE WHEN r.estado = 'pendiente' THEN r.id_reserva END) as pendientes,
        ROUND(
            COUNT(DISTINCT CASE WHEN r.estado = 'cancelada' THEN r.id_reserva END) / 
            COUNT(DISTINCT r.id_reserva) * 100, 2
        ) as tasa_cancelacion
    FROM Reserva r
    GROUP BY DATE(r.fecha_reserva)
    ORDER BY fecha DESC;
    """
    ejecutar_query(conn, query, "QUERY 15: Análisis de Cancelaciones")

# ===== NUEVAS QUERIES CON WHERE =====

def query_16_pedidos_completados_donde(conn):
    """Pedidos completados con WHERE"""
    query = """
    SELECT 
        p.codigo_pedido,
        c.nombre as cliente,
        m.nombre as mesero,
        p.fecha_pedido,
        ROUND(SUM(dp.cantidad * dp.precio_unitario), 2) as total
    FROM Pedido p
    INNER JOIN Reserva r ON p.id_reserva = r.id_reserva
    INNER JOIN Cliente c ON r.id_cliente = c.id_cliente
    INNER JOIN Mesero m ON p.id_mesero = m.id_mesero
    LEFT JOIN DetallePedido dp ON p.id_pedido = dp.id_pedido
    WHERE p.estado = 'completado'
    GROUP BY p.id_pedido, p.codigo_pedido, c.nombre, m.nombre, p.fecha_pedido
    ORDER BY p.fecha_pedido DESC;
    """
    ejecutar_query(conn, query, "QUERY 16: Pedidos Completados (WHERE estado = 'completado')")

def query_17_clientes_por_telefono(conn):
    """Clientes con teléfono específico usando WHERE"""
    query = """
    SELECT 
        c.codigo_cliente,
        c.nombre,
        c.telefono,
        c.correo,
        COUNT(DISTINCT r.id_reserva) as num_reservas,
        ROUND(SUM(pa.monto), 2) as gasto_total
    FROM Cliente c
    LEFT JOIN Reserva r ON c.id_cliente = r.id_cliente
    LEFT JOIN Pedido p ON r.id_reserva = p.id_reserva
    LEFT JOIN Pago pa ON p.id_pedido = pa.id_pedido
    WHERE c.telefono LIKE '321%'
    GROUP BY c.id_cliente, c.codigo_cliente, c.nombre, c.telefono, c.correo
    ORDER BY gasto_total DESC;
    """
    ejecutar_query(conn, query, "QUERY 17: Clientes con Teléfono 321 (WHERE telefono LIKE '321%')")

def query_18_platos_caros(conn):
    """Platos con precio mayor a $15 usando WHERE"""
    query = """
    SELECT 
        p.codigo_plato,
        p.nombre,
        c.nombre as categoria,
        p.precio,
        SUM(dp.cantidad) as veces_vendido,
        ROUND(SUM(dp.cantidad * dp.precio_unitario), 2) as ingresos_totales
    FROM Plato p
    INNER JOIN CategoriaPlato c ON p.id_categoria = c.id_categoria
    LEFT JOIN DetallePedido dp ON p.id_plato = dp.id_plato
    WHERE p.precio > 15.00
    GROUP BY p.id_plato, p.codigo_plato, p.nombre, c.nombre, p.precio
    ORDER BY p.precio DESC;
    """
    ejecutar_query(conn, query, "QUERY 18: Platos Caros (WHERE precio > 15.00)")

def query_19_reservas_confirmadas_fecha(conn):
    """Reservas confirmadas en una fecha específica usando WHERE"""
    query = """
    SELECT 
        r.codigo_reserva,
        c.nombre as cliente,
        m.codigo_mesa,
        m.capacidad,
        t.hora_inicio,
        t.hora_fin,
        r.estado
    FROM Reserva r
    INNER JOIN Cliente c ON r.id_cliente = c.id_cliente
    INNER JOIN Mesa m ON r.id_mesa = m.id_mesa
    INNER JOIN Turno t ON r.id_turno = t.id_turno
    WHERE r.estado = 'confirmada' AND DATE(r.fecha_reserva) = '2025-11-18'
    ORDER BY t.hora_inicio;
    """
    ejecutar_query(conn, query, "QUERY 19: Reservas Confirmadas del 18-11-2025 (WHERE fecha y estado)")

def query_20_pagos_por_tarjeta(conn):
    """Pagos realizados con tarjeta usando WHERE"""
    query = """
    SELECT 
        pa.codigo_pago,
        p.codigo_pedido,
        c.nombre as cliente,
        pa.fecha_pago,
        pa.monto,
        m.nombre as mesero
    FROM Pago pa
    INNER JOIN Pedido p ON pa.id_pedido = p.id_pedido
    INNER JOIN Reserva r ON p.id_reserva = r.id_reserva
    INNER JOIN Cliente c ON r.id_cliente = c.id_cliente
    INNER JOIN Mesero m ON p.id_mesero = m.id_mesero
    WHERE pa.metodo = 'Tarjeta'
    ORDER BY pa.fecha_pago DESC, pa.monto DESC;
    """
    ejecutar_query(conn, query, "QUERY 20: Pagos con Tarjeta (WHERE metodo = 'Tarjeta')")

def query_21_meseros_sin_jefe(conn):
    """Meseros principales (sin jefe) usando WHERE"""
    query = """
    SELECT 
        m.codigo_mesero,
        m.nombre,
        m.telefono,
        m.correo,
        COUNT(DISTINCT p.id_pedido) as pedidos_atendidos,
        COUNT(DISTINCT subordinado.id_mesero) as subordinados
    FROM Mesero m
    LEFT JOIN Pedido p ON m.id_mesero = p.id_mesero
    LEFT JOIN Mesero subordinado ON m.id_mesero = subordinado.id_jefe
    WHERE m.id_jefe IS NULL
    GROUP BY m.id_mesero, m.codigo_mesero, m.nombre, m.telefono, m.correo
    ORDER BY pedidos_atendidos DESC;
    """
    ejecutar_query(conn, query, "QUERY 21: Meseros Principales (WHERE id_jefe IS NULL)")

def query_22_mesas_grande_capacidad(conn):
    """Mesas con capacidad mayor a 6 personas usando WHERE"""
    query = """
    SELECT 
        m.codigo_mesa,
        m.capacidad,
        COUNT(DISTINCT r.id_reserva) as reservas_totales,
        SUM(CASE WHEN r.estado = 'confirmada' THEN 1 ELSE 0 END) as confirmadas,
        ROUND(COUNT(DISTINCT r.id_reserva) / COUNT(DISTINCT r.id_reserva) * 100, 2) as tasa_ocupacion
    FROM Mesa m
    LEFT JOIN Reserva r ON m.id_mesa = r.id_mesa
    WHERE m.capacidad > 6
    GROUP BY m.id_mesa, m.codigo_mesa, m.capacidad
    ORDER BY m.capacidad DESC, reservas_totales DESC;
    """
    ejecutar_query(conn, query, "QUERY 22: Mesas Grandes (WHERE capacidad > 6)")

def query_23_categoria_especifica(conn):
    """Platos de una categoría específica usando WHERE"""
    query = """
    SELECT 
        p.codigo_plato,
        p.nombre,
        p.descripcion,
        p.precio,
        SUM(dp.cantidad) as veces_vendido,
        ROUND(SUM(dp.cantidad * dp.precio_unitario), 2) as ingresos
    FROM Plato p
    INNER JOIN CategoriaPlato c ON p.id_categoria = c.id_categoria
    LEFT JOIN DetallePedido dp ON p.id_plato = dp.id_plato
    WHERE c.nombre = 'Mariscos'
    GROUP BY p.id_plato, p.codigo_plato, p.nombre, p.descripcion, p.precio
    ORDER BY ingresos DESC;
    """
    ejecutar_query(conn, query, "QUERY 23: Platos de Mariscos (WHERE categoria = 'Mariscos')")

def query_24_clientes_sin_reservas(conn):
    """Clientes sin reservas usando WHERE"""
    query = """
    SELECT 
        c.codigo_cliente,
        c.nombre,
        c.telefono,
        c.correo
    FROM Cliente c
    WHERE c.id_cliente NOT IN (SELECT DISTINCT id_cliente FROM Reserva)
    ORDER BY c.nombre;
    """
    ejecutar_query(conn, query, "QUERY 24: Clientes sin Reservas (WHERE NOT IN)")

def query_25_ingresos_rango_fechas(conn):
    """Ingresos en un rango de fechas usando WHERE"""
    query = """
    SELECT 
        DATE(pa.fecha_pago) as fecha,
        COUNT(DISTINCT pa.id_pago) as transacciones,
        ROUND(SUM(pa.monto), 2) as ingresos,
        ROUND(AVG(pa.monto), 2) as ticket_promedio
    FROM Pago pa
    WHERE pa.fecha_pago BETWEEN '2025-11-20' AND '2025-11-25'
    GROUP BY DATE(pa.fecha_pago)
    ORDER BY fecha;
    """
    ejecutar_query(conn, query, "QUERY 25: Ingresos 20-11 al 25-11 (WHERE BETWEEN)")

def query_26_meseros_con_ingresos_altos(conn):
    """Meseros que generaron más de $100 usando WHERE y HAVING"""
    query = """
    SELECT 
        m.codigo_mesero,
        m.nombre,
        COUNT(DISTINCT p.id_pedido) as pedidos,
        ROUND(SUM(pa.monto), 2) as ingresos_generados
    FROM Mesero m
    INNER JOIN Pedido p ON m.id_mesero = p.id_mesero
    INNER JOIN Pago pa ON p.id_pedido = pa.id_pedido
    WHERE p.estado = 'completado'
    GROUP BY m.id_mesero, m.codigo_mesero, m.nombre
    HAVING SUM(pa.monto) > 100
    ORDER BY ingresos_generados DESC;
    """
    ejecutar_query(conn, query, "QUERY 26: Meseros con Ingresos > $100 (WHERE + HAVING)")

def query_27_turnos_matutinos(conn):
    """Turnos de mañana con sus ingresos usando WHERE"""
    query = """
    SELECT 
        t.codigo_turno,
        DATE(t.fecha) as fecha,
        t.hora_inicio,
        COUNT(DISTINCT r.id_reserva) as reservas,
        COUNT(DISTINCT p.id_pedido) as pedidos,
        ROUND(SUM(pa.monto), 2) as ingresos
    FROM Turno t
    LEFT JOIN Reserva r ON t.id_turno = r.id_turno
    LEFT JOIN Pedido p ON r.id_reserva = p.id_reserva
    LEFT JOIN Pago pa ON p.id_pedido = pa.id_pedido
    WHERE HOUR(t.hora_inicio) < 12
    GROUP BY t.id_turno, t.codigo_turno, DATE(t.fecha), t.hora_inicio
    ORDER BY t.fecha DESC, t.hora_inicio;
    """
    ejecutar_query(conn, query, "QUERY 27: Turnos Matutinos (WHERE HOUR < 12)")

def query_28_platos_economicos(conn):
    """Platos económicos menores a $10 usando WHERE"""
    query = """
    SELECT 
        p.codigo_plato,
        p.nombre,
        c.nombre as categoria,
        p.precio,
        COUNT(DISTINCT dp.id_pedido) as veces_vendido,
        ROUND(SUM(dp.cantidad), 2) as total_items_vendidos
    FROM Plato p
    INNER JOIN CategoriaPlato c ON p.id_categoria = c.id_categoria
    LEFT JOIN DetallePedido dp ON p.id_plato = dp.id_plato
    WHERE p.precio < 10.00
    GROUP BY p.id_plato, p.codigo_plato, p.nombre, c.nombre, p.precio
    ORDER BY p.precio ASC;
    """
    ejecutar_query(conn, query, "QUERY 28: Platos Económicos (WHERE precio < 10)")

def query_29_reservas_pendientes(conn):
    """Reservas pendientes de confirmación usando WHERE"""
    query = """
    SELECT 
        r.codigo_reserva,
        c.nombre as cliente,
        m.codigo_mesa,
        DATE(r.fecha_reserva) as fecha_reserva,
        t.hora_inicio,
        COUNT(DISTINCT p.id_pedido) as pedidos
    FROM Reserva r
    INNER JOIN Cliente c ON r.id_cliente = c.id_cliente
    INNER JOIN Mesa m ON r.id_mesa = m.id_mesa
    INNER JOIN Turno t ON r.id_turno = t.id_turno
    LEFT JOIN Pedido p ON r.id_reserva = p.id_reserva
    WHERE r.estado = 'pendiente'
    GROUP BY r.id_reserva, r.codigo_reserva, c.nombre, m.codigo_mesa, r.fecha_reserva, t.hora_inicio
    ORDER BY r.fecha_reserva;
    """
    ejecutar_query(conn, query, "QUERY 29: Reservas Pendientes (WHERE estado = 'pendiente')")

def query_30_clientes_con_email(conn):
    """Clientes que proporcionaron email usando WHERE"""
    query = """
    SELECT 
        c.codigo_cliente,
        c.nombre,
        c.correo,
        c.telefono,
        COUNT(DISTINCT r.id_reserva) as reservas,
        ROUND(SUM(pa.monto), 2) as gasto_total
    FROM Cliente c
    LEFT JOIN Reserva r ON c.id_cliente = r.id_cliente
    LEFT JOIN Pedido p ON r.id_reserva = p.id_reserva
    LEFT JOIN Pago pa ON p.id_pedido = pa.id_pedido
    WHERE c.correo IS NOT NULL AND c.correo != ''
    GROUP BY c.id_cliente, c.codigo_cliente, c.nombre, c.correo, c.telefono
    ORDER BY gasto_total DESC;
    """
    ejecutar_query(conn, query, "QUERY 30: Clientes con Email (WHERE correo IS NOT NULL)")

def ejecutar_todas_las_queries(conn):
    """Ejecuta todas las 30 queries"""
    print("\n" + "🔍"*40)
    print("EJECUTANDO 30 QUERIES (15 ORIGINALES + 15 CON WHERE)")
    print("🔍"*40)
    
    # Queries originales
    query_1_ingresos_por_mesero(conn)
    query_2_platos_mas_vendidos(conn)
    query_3_ocupacion_mesas(conn)
    query_4_clientes_frecuentes(conn)
    query_5_categorias_mas_vendidas(conn)
    query_6_analisis_turnos(conn)
    query_7_metodos_pago(conn)
    query_8_estado_pedidos(conn)
    query_9_reservas_por_estado(conn)
    query_10_meseros_jerarquia(conn)
    query_11_ingresos_diarios(conn)
    query_12_platos_por_pedido(conn)
    query_13_capacidad_mesas_optimizacion(conn)
    query_14_comparativa_turnos(conn)
    query_15_cancellations_analysis(conn)
    
    # Nuevas queries con WHERE
    query_16_pedidos_completados_donde(conn)
    query_17_clientes_por_telefono(conn)
    query_18_platos_caros(conn)
    query_19_reservas_confirmadas_fecha(conn)
    query_20_pagos_por_tarjeta(conn)
    query_21_meseros_sin_jefe(conn)
    query_22_mesas_grande_capacidad(conn)
    query_23_categoria_especifica(conn)
    query_24_clientes_sin_reservas(conn)
    query_25_ingresos_rango_fechas(conn)
    query_26_meseros_con_ingresos_altos(conn)
    query_27_turnos_matutinos(conn)
    query_28_platos_economicos(conn)
    query_29_reservas_pendientes(conn)
    query_30_clientes_con_email(conn)
    
    print("\n" + ":3"*40)
    print("¡TODAS LAS 30 QUERIES SE HAN EJECUTADO CORRECTAMENTE!")
    print(":3"*40 + "\n")

if __name__ == "__main__":
    conn = conectar_bd()
    ejecutar_todas_las_queries(conn)
    conn.close()