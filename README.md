# bases-project
Proyecto de bases de datos I 

# Autores
Diego Combariza
Camilo Rodriguez
Karolain Giraldo 

## Tema seleccionado:
Gestión de reservas y pedidos en restaurante, incluyendo mesas, clientes, turnos, platos, meseros y pagos.

### Alcance y objetivos:
Registrar clientes, reservas, mesas y turnos disponibles.
Permitir gestión y consulta de pedidos y pagos.
Asignación de mesero responsable a cada pedido.
Soportar jerarquía interna de meseros (mesero/jefe).

### Entidades principales:
CategoriaPlato: Agrupa los tipos de platos.
Plato: Elementos del menú, vinculados a categorías.
Mesa: Ubicaciones físicas con capacidad.
Cliente: Personas que reservan y consumen.
Turno: Franja horaria o fecha y hora de la reserva.
Reserva: Acción de reservar mesa/turno para cliente.
Mesero: Empleados de atención, pueden tener jefe.
Pedido: Pedido realizado durante la visita, atendido por mesero.
DetallePedido: Platos pedidos y cantidad por pedido.
Pago: Registro de monto y método de pago de cada pedido.

### Relaciones entre entidades:
Un cliente realiza muchas reservas, cada reserva es para una mesa y un turno.
Una reserva genera un pedido, que es atendido por un mesero.
Un mesero puede tener un jefe mesero, relación recursiva.
Un pedido consiste en varios detallePedido (platos y cantidad).
Un plato pertenece a una categoriaPlato.
Un pedido puede tener varios pagos asociados.
