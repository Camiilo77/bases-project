# ARCHIVO DE CONSULTAS SQL - 30 QUERIES
from Tables import conectar_bd

def ejecutar_query(conn, query, descripcion):
    """Función auxiliar para ejecutar y mostrar resultados"""
    print(f"\n{'='*80}")
    print(f"📊 {descripcion}")
    print(f"{'='*80}")
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        
        if resultados:
            columnas = [i[0] for i in cursor.description]
            print(f"\n{' | '.join(columnas)}")
            print("-" * 120)
            
            for fila in resultados[:20]:  # Mostrar máximo 20 filas
                print(f"{' | '.join(str(x) for x in fila)}")
            
            if len(resultados) > 20:
                print(f"\n... {len(resultados) - 20} filas más ...")
            print(f"\n✅ Total de registros: {len(resultados)}")
        else:
            print("⚠️ No hay resultados")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        cursor.close()

# ========== QUERIES 1-10: ANÁLISIS GENERAL ==========

def query_1_top_platos_vendidos(conn):
    """Top 10 platos más vendidos con ingresos"""
    query = """
    SELECT 
        p.codigo_plato,
        p.nombre,
        c.nombre as categoria,
        p.precio,
        COUNT(dp.id_detalle) as veces_pedido,
        SUM(dp.cantidad) as unidades_vendidas,
        ROUND(SUM(dp.cantidad * dp.precio_unitario), 2) as ingresos_totales
    FROM Plato p
    INNER JOIN CategoriaPlato c ON p.id_categoria = c.id_categoria
    LEFT JOIN DetallePedido dp ON p.id_plato = dp.id_plato
    GROUP BY p.id_plato, p.codigo_plato, p.nombre, c.nombre, p.precio
    ORDER BY unidades_vendidas DESC
    LIMIT 10;
    """
    ejecutar_query(conn, query, "QUERY 1: Top 10 Platos Más Vendidos")

def query_2_ingresos_por_categoria(conn):
    """Ingresos totales por categoría de platos"""
    query = """
    SELECT 
        c.codigo_categoria,
        c.nombre as categoria,
        COUNT(DISTINCT p.id_plato) as num_platos,
        COUNT(dp.id_detalle) as veces_pedido,
        SUM(dp.cantidad) as unidades_vendidas,
        ROUND(SUM(dp.cantidad * dp.precio_unitario), 2) as ingresos_totales,
        ROUND(AVG(dp.precio_unitario), 2) as precio_promedio
    FROM CategoriaPlato c
    INNER JOIN Plato p ON c.id_categoria = p.id_categoria
    LEFT JOIN DetallePedido dp ON p.id_plato = dp.id_plato
    GROUP BY c.id_categoria, c.codigo_categoria, c.nombre
    ORDER BY ingresos_totales DESC;
    """
    ejecutar_query(conn, query, "QUERY 2: Ingresos por Categoría")

def query_3_meseros_top_desempenio(conn):
    """Meseros con mejor desempeño (más pedidos e ingresos)"""
    query = """
    SELECT 
        m.codigo_mesero,
        m.nombre,
        m.telefono,
        COUNT(DISTINCT p.id_pedido) as total_pedidos,
        SUM(p.total) as ingresos_generados,
        ROUND(AVG(p.total), 2) as ticket_promedio,
        COUNT(DISTINCT mp.id) as asignaciones
    FROM Mesero m
    LEFT JOIN Pedido p ON m.id_mesero = p.id_mesero
    LEFT JOIN MeseroPedido mp ON m.id_mesero = mp.id_mesero
    GROUP BY m.id_mesero, m.codigo_mesero, m.nombre, m.telefono
    HAVING total_pedidos > 0
    ORDER BY ingresos_generados DESC
    LIMIT 15;
    """
    ejecutar_query(conn, query, "QUERY 3: Top 15 Meseros por Desempeño")

def query_4_clientes_frecuentes(conn):
    """Clientes más frecuentes y su gasto total"""
    query = """
    SELECT 
        c.codigo_cliente,
        c.nombre,
        c.telefono,
        c.correo,
        COUNT(DISTINCT r.id_reserva) as num_reservas,
        COUNT(DISTINCT p.id_pedido) as num_pedidos,
        ROUND(SUM(pa.monto), 2) as gasto_total,
        ROUND(AVG(pa.monto), 2) as gasto_promedio
    FROM Cliente c
    INNER JOIN Reserva r ON c.id_cliente = r.id_cliente
    LEFT JOIN Pedido p ON r.id_reserva = p.id_reserva
    LEFT JOIN Pago pa ON p.id_pedido = pa.id_pedido
    GROUP BY c.id_cliente, c.codigo_cliente, c.nombre, c.telefono, c.correo
    ORDER BY gasto_total DESC
    LIMIT 15;
    """
    ejecutar_query(conn, query, "QUERY 4: Top 15 Clientes Frecuentes")

def query_5_ocupacion_mesas(conn):
    """Análisis de ocupación de mesas"""
    query = """
    SELECT 
        m.codigo_mesa,
        m.capacidad,
        m.ubicacion,
        m.estado,
        COUNT(DISTINCT r.id_reserva) as num_reservas,
        COUNT(DISTINCT p.id_pedido) as num_pedidos,
        ROUND(SUM(p.total), 2) as ingresos_generados
    FROM Mesa m
    LEFT JOIN Reserva r ON m.id_mesa = r.id_mesa
    LEFT JOIN Pedido p ON r.id_reserva = p.id_reserva
    GROUP BY m.id_mesa, m.codigo_mesa, m.capacidad, m.ubicacion, m.estado
    ORDER BY ingresos_generados DESC
    LIMIT 20;
    """
    ejecutar_query(conn, query, "QUERY 5: Análisis de Ocupación de Mesas")

def query_6_analisis_turnos(conn):
    """Análisis de turnos: reservas y pedidos por turno"""
    query = """
    SELECT 
        t.codigo_turno,
        t.fecha,
        t.hora_inicio,
        t.hora_fin,
        COUNT(DISTINCT r.id_reserva) as num_reservas,
        COUNT(DISTINCT p.id_pedido) as num_pedidos,
        ROUND(SUM(p.total), 2) as ingresos_turno,
        ROUND(AVG(p.total), 2) as ticket_promedio
    FROM Turno t
    LEFT JOIN Reserva r ON t.id_turno = r.id_turno
    LEFT JOIN Pedido p ON r.id_reserva = p.id_reserva
    GROUP BY t.id_turno, t.codigo_turno, t.fecha, t.hora_inicio, t.hora_fin
    ORDER BY t.fecha DESC, t.hora_inicio
    LIMIT 20;
    """
    ejecutar_query(conn, query, "QUERY 6: Análisis de Turnos")

def query_7_metodos_pago_distribucion(conn):
    """Distribución de métodos de pago y montos"""
    query = """
    SELECT 
        metodo,
        COUNT(*) as num_transacciones,
        ROUND(SUM(monto), 2) as monto_total,
        ROUND(AVG(monto), 2) as promedio_transaccion,
        ROUND(MIN(monto), 2) as monto_minimo,
        ROUND(MAX(monto), 2) as monto_maximo,
        ROUND((SUM(monto) / (SELECT SUM(monto) FROM Pago)) * 100, 2) as porcentaje_total
    FROM Pago
    GROUP BY metodo
    ORDER BY monto_total DESC;
    """
    ejecutar_query(conn, query, "QUERY 7: Distribución de Métodos de Pago")

def query_8_estados_pedidos(conn):
    """Distribución de pedidos por estado"""
    query = """
    SELECT 
        estado,
        COUNT(*) as cantidad_pedidos,
        ROUND((COUNT(*) / (SELECT COUNT(*) FROM Pedido)) * 100, 2) as porcentaje,
        ROUND(SUM(total), 2) as monto_total,
        ROUND(AVG(total), 2) as monto_promedio
    FROM Pedido
    GROUP BY estado
    ORDER BY cantidad_pedidos DESC;
    """
    ejecutar_query(conn, query, "QUERY 8: Distribución de Estados de Pedidos")

def query_9_reservas_por_estado(conn):
    """Distribución de reservas por estado"""
    query = """
    SELECT 
        estado,
        COUNT(*) as total_reservas,
        ROUND((COUNT(*) / (SELECT COUNT(*) FROM Reserva)) * 100, 2) as porcentaje,
        MIN(fecha_reserva) as fecha_primera,
        MAX(fecha_reserva) as fecha_ultima,
        COUNT(DISTINCT id_cliente) as clientes_unicos
    FROM Reserva
    GROUP BY estado
    ORDER BY total_reservas DESC;
    """
    ejecutar_query(conn, query, "QUERY 9: Distribución de Reservas por Estado")

def query_10_jerarquia_meseros(conn):
    """Estructura jerárquica de meseros con su desempeño"""
    query = """
    SELECT 
        m.codigo_mesero,
        m.nombre as mesero,
        COALESCE(jefe.nombre, 'JEFE PRINCIPAL') as jefe,
        m.activo,
        COUNT(DISTINCT p.id_pedido) as pedidos_atendidos,
        ROUND(SUM(p.total), 2) as ingresos_generados
    FROM Mesero m
    LEFT JOIN Mesero jefe ON m.id_jefe = jefe.id_mesero
    LEFT JOIN Pedido p ON m.id_mesero = p.id_mesero
    GROUP BY m.id_mesero, m.codigo_mesero, m.nombre, jefe.nombre, m.activo
    ORDER BY m.id_jefe IS NULL DESC, jefe.nombre, ingresos_generados DESC
    LIMIT 30;
    """
    ejecutar_query(conn, query, "QUERY 10: Jerarquía de Meseros y Desempeño")

# ========== QUERIES 11-20: ANÁLISIS CON WHERE ==========

def query_11_platos_precio_alto(conn):
    """Platos con precio mayor a $30"""
    query = """
    SELECT 
        p.codigo_plato,
        p.nombre,
        c.nombre as categoria,
        p.precio,
        p.tiempo_preparacion_min,
        COUNT(dp.id_detalle) as veces_vendido,
        ROUND(SUM(dp.cantidad * dp.precio_unitario), 2) as ingresos
    FROM Plato p
    INNER JOIN CategoriaPlato c ON p.id_categoria = c.id_categoria
    LEFT JOIN DetallePedido dp ON p.id_plato = dp.id_plato
    WHERE p.precio > 30.00
    GROUP BY p.id_plato, p.codigo_plato, p.nombre, c.nombre, p.precio, p.tiempo_preparacion_min
    ORDER BY p.precio DESC;
    """
    ejecutar_query(conn, query, "QUERY 11: Platos con Precio > $30 (WHERE)")

def query_12_reservas_confirmadas(conn):
    """Reservas confirmadas únicamente"""
    query = """
    SELECT 
        r.codigo_reserva,
        c.nombre as cliente,
        m.codigo_mesa,
        m.capacidad,
        r.num_personas,
        t.fecha,
        t.hora_inicio,
        r.estado
    FROM Reserva r
    INNER JOIN Cliente c ON r.id_cliente = c.id_cliente
    INNER JOIN Mesa m ON r.id_mesa = m.id_mesa
    INNER JOIN Turno t ON r.id_turno = t.id_turno
    WHERE r.estado = 'confirmada'
    ORDER BY t.fecha DESC, t.hora_inicio;
    """
    ejecutar_query(conn, query, "QUERY 12: Reservas Confirmadas (WHERE estado)")

def query_13_pagos_efectivo(conn):
    """Pagos realizados en efectivo"""
    query = """
    SELECT 
        pa.codigo_pago,
        p.codigo_pedido,
        c.nombre as cliente,
        pa.fecha_pago,
        pa.monto,
        pa.metodo
    FROM Pago pa
    INNER JOIN Pedido p ON pa.id_pedido = p.id_pedido
    INNER JOIN Reserva r ON p.id_reserva = r.id_reserva
    INNER JOIN Cliente c ON r.id_cliente = c.id_cliente
    WHERE pa.metodo = 'efectivo'
    ORDER BY pa.monto DESC;
    """
    ejecutar_query(conn, query, "QUERY 13: Pagos en Efectivo (WHERE metodo)")

def query_14_mesas_capacidad_4(conn):
    """Mesas con capacidad de 4 personas"""
    query = """
    SELECT 
        m.codigo_mesa,
        m.capacidad,
        m.ubicacion,
        m.estado,
        COUNT(DISTINCT r.id_reserva) as num_reservas,
        ROUND(SUM(p.total), 2) as ingresos_generados
    FROM Mesa m
    LEFT JOIN Reserva r ON m.id_mesa = r.id_mesa
    LEFT JOIN Pedido p ON r.id_reserva = p.id_reserva
    WHERE m.capacidad = 4
    GROUP BY m.id_mesa, m.codigo_mesa, m.capacidad, m.ubicacion, m.estado
    ORDER BY ingresos_generados DESC;
    """
    ejecutar_query(conn, query, "QUERY 14: Mesas de Capacidad 4 (WHERE)")

def query_15_meseros_sin_jefe(conn):
    """Meseros que son jefes (sin supervisor)"""
    query = """
    SELECT 
        m.codigo_mesero,
        m.nombre,
        m.telefono,
        m.correo,
        COUNT(DISTINCT p.id_pedido) as pedidos_atendidos,
        COUNT(DISTINCT subordinado.id_mesero) as num_subordinados,
        ROUND(SUM(p.total), 2) as ingresos_generados
    FROM Mesero m
    LEFT JOIN Pedido p ON m.id_mesero = p.id_mesero
    LEFT JOIN Mesero subordinado ON m.id_mesero = subordinado.id_jefe
    WHERE m.id_jefe IS NULL
    GROUP BY m.id_mesero, m.codigo_mesero, m.nombre, m.telefono, m.correo
    ORDER BY ingresos_generados DESC;
    """
    ejecutar_query(conn, query, "QUERY 15: Meseros Jefes (WHERE id_jefe IS NULL)")

def query_16_pedidos_pagados(conn):
    """Pedidos con estado 'pagado'"""
    query = """
    SELECT 
        p.codigo_pedido,
        c.nombre as cliente,
        m.nombre as mesero,
        p.fecha_pedido,
        p.total,
        p.estado
    FROM Pedido p
    INNER JOIN Reserva r ON p.id_reserva = r.id_reserva
    INNER JOIN Cliente c ON r.id_cliente = c.id_cliente
    INNER JOIN Mesero m ON p.id_mesero = m.id_mesero
    WHERE p.estado = 'pagado'
    ORDER BY p.total DESC;
    """
    ejecutar_query(conn, query, "QUERY 16: Pedidos Pagados (WHERE estado)")

def query_17_categorias_especificas(conn):
    """Platos de categorías específicas (Entradas, Sopas, Ensaladas)"""
    query = """
    SELECT 
        p.codigo_plato,
        p.nombre,
        c.nombre as categoria,
        p.precio,
        p.descripcion
    FROM Plato p
    INNER JOIN CategoriaPlato c ON p.id_categoria = c.id_categoria
    WHERE c.nombre IN ('Entradas', 'Sopas', 'Ensaladas')
    ORDER BY c.nombre, p.precio DESC;
    """
    ejecutar_query(conn, query, "QUERY 17: Platos de Entradas, Sopas y Ensaladas (WHERE IN)")

def query_18_clientes_con_email(conn):
    """Clientes que tienen correo electrónico"""
    query = """
    SELECT 
        c.codigo_cliente,
        c.nombre,
        c.telefono,
        c.correo,
        COUNT(DISTINCT r.id_reserva) as num_reservas
    FROM Cliente c
    LEFT JOIN Reserva r ON c.id_cliente = r.id_cliente
    WHERE c.correo IS NOT NULL AND c.correo != ''
    GROUP BY c.id_cliente, c.codigo_cliente, c.nombre, c.telefono, c.correo
    ORDER BY num_reservas DESC;
    """
    ejecutar_query(conn, query, "QUERY 18: Clientes con Email (WHERE IS NOT NULL)")

def query_19_turnos_noche(conn):
    """Turnos nocturnos (después de las 18:00)"""
    query = """
    SELECT 
        t.codigo_turno,
        t.fecha,
        t.hora_inicio,
        t.hora_fin,
        COUNT(DISTINCT r.id_reserva) as num_reservas,
        ROUND(SUM(p.total), 2) as ingresos
    FROM Turno t
    LEFT JOIN Reserva r ON t.id_turno = r.id_turno
    LEFT JOIN Pedido p ON r.id_reserva = p.id_reserva
    WHERE HOUR(t.hora_inicio) >= 18
    GROUP BY t.id_turno, t.codigo_turno, t.fecha, t.hora_inicio, t.hora_fin
    ORDER BY t.fecha DESC;
    """
    ejecutar_query(conn, query, "QUERY 19: Turnos Nocturnos (WHERE HOUR >= 18)")

def query_20_platos_preparacion_rapida(conn):
    """Platos con tiempo de preparación menor a 15 minutos"""
    query = """
    SELECT 
        p.codigo_plato,
        p.nombre,
        c.nombre as categoria,
        p.tiempo_preparacion_min,
        p.precio,
        COUNT(dp.id_detalle) as veces_vendido
    FROM Plato p
    INNER JOIN CategoriaPlato c ON p.id_categoria = c.id_categoria
    LEFT JOIN DetallePedido dp ON p.id_plato = dp.id_plato
    WHERE p.tiempo_preparacion_min < 15
    GROUP BY p.id_plato, p.codigo_plato, p.nombre, c.nombre, p.tiempo_preparacion_min, p.precio
    ORDER BY veces_vendido DESC;
    """
    ejecutar_query(conn, query, "QUERY 20: Platos de Preparación Rápida (WHERE tiempo < 15)")

# ========== QUERIES 21-30: ANÁLISIS AVANZADOS ==========

def query_21_ingresos_por_fecha(conn):
    """Ingresos totales agrupados por fecha"""
    query = """
    SELECT 
        pa.fecha_pago,
        COUNT(DISTINCT pa.id_pago) as num_transacciones,
        COUNT(DISTINCT p.id_pedido) as num_pedidos,
        ROUND(SUM(pa.monto), 2) as ingresos_diarios,
        ROUND(AVG(pa.monto), 2) as ticket_promedio
    FROM Pago pa
    LEFT JOIN Pedido p ON pa.id_pedido = p.id_pedido
    GROUP BY pa.fecha_pago
    ORDER BY pa.fecha_pago DESC;
    """
    ejecutar_query(conn, query, "QUERY 21: Ingresos por Fecha")

def query_22_mesas_por_ubicacion(conn):
    """Análisis de mesas agrupadas por ubicación"""
    query = """
    SELECT 
        m.ubicacion,
        COUNT(DISTINCT m.id_mesa) as num_mesas,
        ROUND(AVG(m.capacidad), 1) as capacidad_promedio,
        COUNT(DISTINCT r.id_reserva) as total_reservas,
        ROUND(SUM(p.total), 2) as ingresos_totales
    FROM Mesa m
    LEFT JOIN Reserva r ON m.id_mesa = r.id_mesa
    LEFT JOIN Pedido p ON r.id_reserva = p.id_reserva
    GROUP BY m.ubicacion
    ORDER BY ingresos_totales DESC;
    """
    ejecutar_query(conn, query, "QUERY 22: Análisis de Mesas por Ubicación")

def query_23_detalle_pedidos_completo(conn):
    """Detalle completo de pedidos con platos"""
    query = """
    SELECT 
        p.codigo_pedido,
        c.nombre as cliente,
        pl.nombre as plato,
        dp.cantidad,
        dp.precio_unitario,
        ROUND(dp.cantidad * dp.precio_unitario, 2) as subtotal,
        p.fecha_pedido
    FROM DetallePedido dp
    INNER JOIN Pedido p ON dp.id_pedido = p.id_pedido
    INNER JOIN Plato pl ON dp.id_plato = pl.id_plato
    INNER JOIN Reserva r ON p.id_reserva = r.id_reserva
    INNER JOIN Cliente c ON r.id_cliente = c.id_cliente
    ORDER BY p.fecha_pedido DESC, p.codigo_pedido
    LIMIT 30;
    """
    ejecutar_query(conn, query, "QUERY 23: Detalle Completo de Pedidos")

def query_24_meseros_por_rol(conn):
    """Meseros agrupados por rol en pedidos"""
    query = """
    SELECT 
        mp.rol,
        COUNT(DISTINCT mp.id_mesero) as num_meseros,
        COUNT(DISTINCT mp.id_pedido) as num_asignaciones,
        m.nombre as ejemplo_mesero
    FROM MeseroPedido mp
    INNER JOIN Mesero m ON mp.id_mesero = m.id_mesero
    GROUP BY mp.rol, m.nombre
    ORDER BY num_asignaciones DESC
    LIMIT 20;
    """
    ejecutar_query(conn, query, "QUERY 24: Meseros por Rol en Pedidos")

def query_25_reservas_multiples_clientes(conn):
    """Clientes con más de 1 reserva"""
    query = """
    SELECT 
        c.codigo_cliente,
        c.nombre,
        c.telefono,
        COUNT(DISTINCT r.id_reserva) as num_reservas,
        COUNT(DISTINCT p.id_pedido) as num_pedidos,
        ROUND(SUM(pa.monto), 2) as gasto_total
    FROM Cliente c
    INNER JOIN Reserva r ON c.id_cliente = r.id_cliente
    LEFT JOIN Pedido p ON r.id_reserva = p.id_reserva
    LEFT JOIN Pago pa ON p.id_pedido = pa.id_pedido
    GROUP BY c.id_cliente, c.codigo_cliente, c.nombre, c.telefono
    HAVING COUNT(DISTINCT r.id_reserva) > 1
    ORDER BY num_reservas DESC, gasto_total DESC;
    """
    ejecutar_query(conn, query, "QUERY 25: Clientes con Múltiples Reservas (HAVING)")

def query_26_pedidos_alto_valor(conn):
    """Pedidos con valor total mayor a $200"""
    query = """
    SELECT 
        p.codigo_pedido,
        c.nombre as cliente,
        m.nombre as mesero,
        p.fecha_pedido,
        p.total,
        p.estado,
        pa.metodo as metodo_pago
    FROM Pedido p
    INNER JOIN Reserva r ON p.id_reserva = r.id_reserva
    INNER JOIN Cliente c ON r.id_cliente = c.id_cliente
    INNER JOIN Mesero m ON p.id_mesero = m.id_mesero
    LEFT JOIN Pago pa ON p.id_pedido = pa.id_pedido
    WHERE p.total > 200
    ORDER BY p.total DESC;
    """
    ejecutar_query(conn, query, "QUERY 26: Pedidos de Alto Valor (> $200)")

def query_27_platos_no_vendidos(conn):
    """Platos que no han sido vendidos"""
    query = """
    SELECT 
        p.codigo_plato,
        p.nombre,
        c.nombre as categoria,
        p.precio,
        p.descripcion,
        p.disponible
    FROM Plato p
    INNER JOIN CategoriaPlato c ON p.id_categoria = c.id_categoria
    LEFT JOIN DetallePedido dp ON p.id_plato = dp.id_plato
    WHERE dp.id_detalle IS NULL
    ORDER BY p.precio DESC;
    """
    ejecutar_query(conn, query, "QUERY 27: Platos No Vendidos (LEFT JOIN con NULL)")

def query_28_analisis_capacidad_vs_personas(conn):
    """Comparación entre capacidad de mesa y número de personas en reserva"""
    query = """
    SELECT 
        m.codigo_mesa,
        m.capacidad,
        r.num_personas,
        CASE 
            WHEN r.num_personas = m.capacidad THEN 'Uso Óptimo'
            WHEN r.num_personas < m.capacidad THEN 'Subutilizada'
            ELSE 'Sobrecapacidad'
        END as estado_uso,
        COUNT(*) as veces_reservada
    FROM Reserva r
    INNER JOIN Mesa m ON r.id_mesa = m.id_mesa
    GROUP BY m.codigo_mesa, m.capacidad, r.num_personas
    ORDER BY m.codigo_mesa, veces_reservada DESC;
    """
    ejecutar_query(conn, query, "QUERY 28: Análisis de Uso de Capacidad de Mesas")

def query_29_pagos_por_metodo_fecha(conn):
    """Pagos agrupados por método y fecha"""
    query = """
    SELECT 
        pa.fecha_pago,
        pa.metodo,
        COUNT(*) as num_transacciones,
        ROUND(SUM(pa.monto), 2) as monto_total,
        ROUND(AVG(pa.monto), 2) as promedio
    FROM Pago pa
    GROUP BY pa.fecha_pago, pa.metodo
    ORDER BY pa.fecha_pago DESC, monto_total DESC;
    """
    ejecutar_query(conn, query, "QUERY 29: Pagos por Método y Fecha")

def query_30_resumen_completo_restaurante(conn):
    """Resumen general del restaurante"""
    query = """
    SELECT 
        'Total Clientes' as metrica, COUNT(DISTINCT id_cliente) as valor FROM Cliente
    UNION ALL
    SELECT 'Total Meseros', COUNT(DISTINCT id_mesero) FROM Mesero
    UNION ALL
    SELECT 'Total Mesas', COUNT(DISTINCT id_mesa) FROM Mesa
    UNION ALL
    SELECT 'Total Platos', COUNT(DISTINCT id_plato) FROM Plato
    UNION ALL
    SELECT 'Total Categorías', COUNT(DISTINCT id_categoria) FROM CategoriaPlato
    UNION ALL
    SELECT 'Total Reservas', COUNT(DISTINCT id_reserva) FROM Reserva
    UNION ALL
    SELECT 'Total Pedidos', COUNT(DISTINCT id_pedido) FROM Pedido
    UNION ALL
    SELECT 'Total Pagos', COUNT(DISTINCT id_pago) FROM Pago
    UNION ALL
    SELECT 'Ingresos Totales', CAST(ROUND(SUM(monto), 2) AS UNSIGNED) FROM Pago
    UNION ALL
    SELECT 'Ticket Promedio', CAST(ROUND(AVG(monto), 2) AS UNSIGNED) FROM Pago;
    """
    ejecutar_query(conn, query, "QUERY 30: Resumen General del Restaurante")


def query_31_mesas_disponibles_por_turno(conn):
    """Mesas disponibles por turno (no reservadas)"""
    query = """
    SELECT 
        t.codigo_turno,
        t.fecha,
        t.hora_inicio,
        t.hora_fin,
        m.codigo_mesa,
        m.capacidad,
        m.ubicacion,
        m.estado,
        CASE 
            WHEN r.id_reserva IS NULL THEN 'DISPONIBLE'
            ELSE 'RESERVADA'
        END as disponibilidad
    FROM Turno t
    CROSS JOIN Mesa m
    LEFT JOIN Reserva r ON t.id_turno = r.id_turno 
        AND m.id_mesa = r.id_mesa
        AND r.estado NOT IN ('cancelada')
    WHERE m.estado IN ('libre', 'reservada')
    ORDER BY t.fecha DESC, t.hora_inicio, m.codigo_mesa;
    """
    ejecutar_query(conn, query, "QUERY 31: Mesas Disponibles por Turno")

def query_32_mesas_libres_turno_especifico(conn):
    """Mesas disponibles para un turno específico (ejemplo: próximos turnos)"""
    query = """
    SELECT 
        t.codigo_turno,
        t.fecha,
        t.hora_inicio,
        t.hora_fin,
        COUNT(DISTINCT CASE WHEN r.id_reserva IS NULL THEN m.id_mesa END) as mesas_disponibles,
        COUNT(DISTINCT CASE WHEN r.id_reserva IS NOT NULL THEN m.id_mesa END) as mesas_reservadas,
        COUNT(DISTINCT m.id_mesa) as total_mesas,
        GROUP_CONCAT(
            DISTINCT CASE 
                WHEN r.id_reserva IS NULL 
                THEN CONCAT(m.codigo_mesa, ' (Cap: ', m.capacidad, ')')
            END 
            ORDER BY m.codigo_mesa 
            SEPARATOR ', '
        ) as mesas_disponibles_detalle
    FROM Turno t
    CROSS JOIN Mesa m
    LEFT JOIN Reserva r ON t.id_turno = r.id_turno 
        AND m.id_mesa = r.id_mesa
        AND r.estado IN ('confirmada', 'pendiente', 'en_servicio')
    WHERE m.estado IN ('libre', 'reservada')
        AND t.fecha >= CURDATE()
    GROUP BY t.id_turno, t.codigo_turno, t.fecha, t.hora_inicio, t.hora_fin
    ORDER BY t.fecha, t.hora_inicio;
    """
    ejecutar_query(conn, query, "QUERY 32: Resumen de Disponibilidad por Turno")
# ========== FUNCIÓN PRINCIPAL ==========

def ejecutar_todas_las_queries():
    """Ejecuta todas las 30 queries del sistema"""
    conn = conectar_bd()
    if conn is None:
        print("❌ No se pudo conectar a la base de datos")
        return
    
    print("\n" + "🔍"*50)
    print(" EJECUTANDO 30 QUERIES - SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("🔍"*50)
    
    # QUERIES 1-10: Análisis General
    query_1_top_platos_vendidos(conn)
    query_2_ingresos_por_categoria(conn)
    query_3_meseros_top_desempenio(conn)
    query_4_clientes_frecuentes(conn)
    query_5_ocupacion_mesas(conn)
    query_6_analisis_turnos(conn)
    query_7_metodos_pago_distribucion(conn)
    query_8_estados_pedidos(conn)
    query_9_reservas_por_estado(conn)
    query_10_jerarquia_meseros(conn)
    
    # QUERIES 11-20: Análisis con WHERE
    query_11_platos_precio_alto(conn)
    query_12_reservas_confirmadas(conn)
    query_13_pagos_efectivo(conn)
    query_14_mesas_capacidad_4(conn)
    query_15_meseros_sin_jefe(conn)
    query_16_pedidos_pagados(conn)
    query_17_categorias_especificas(conn)
    query_18_clientes_con_email(conn)
    query_19_turnos_noche(conn)
    query_20_platos_preparacion_rapida(conn)
    
    # QUERIES 21-30: Análisis Avanzados
    query_21_ingresos_por_fecha(conn)
    query_22_mesas_por_ubicacion(conn)
    query_23_detalle_pedidos_completo(conn)
    query_24_meseros_por_rol(conn)
    query_25_reservas_multiples_clientes(conn)
    query_26_pedidos_alto_valor(conn)
    query_27_platos_no_vendidos(conn)
    query_28_analisis_capacidad_vs_personas(conn)
    query_29_pagos_por_metodo_fecha(conn)
    query_30_resumen_completo_restaurante(conn)
    
        # QUERIES 31-32: Disponibilidad de Mesas
    query_31_mesas_disponibles_por_turno(conn)
    query_32_mesas_libres_turno_especifico(conn)
    
    conn.close()
    
    print("\n" + "✅"*50)
    print(" ¡TODAS LAS 30 QUERIES EJECUTADAS EXITOSAMENTE!")
    print("✅"*50 + "\n")


if __name__ == "__main__":
    ejecutar_todas_las_queries()
