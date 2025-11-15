CREATE DATABASE restaurante_db;
USE restaurante_db;
CREATE TABLE CategoriaPlato (
  id_categoria INT PRIMARY KEY,
  codigo_categoria VARCHAR(50) NOT NULL UNIQUE,
  nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Plato (
  id_plato INT PRIMARY KEY,
  codigo_plato VARCHAR(50) NOT NULL UNIQUE,
  nombre VARCHAR(50) NOT NULL,
  descripcion VARCHAR(50),
  precio DECIMAL(10,4) NOT NULL,
  id_categoria INT,
  FOREIGN KEY (id_categoria) REFERENCES CategoriaPlato(id_categoria)
);

CREATE TABLE Mesa (
  id_mesa INT PRIMARY KEY,
  codigo_mesa VARCHAR(50) NOT NULL UNIQUE,
  capacidad INT NOT NULL
);

CREATE TABLE Cliente (
  id_cliente INT PRIMARY KEY,
  codigo_cliente VARCHAR(50) NOT NULL UNIQUE,
  nombre VARCHAR(50) NOT NULL,
  telefono VARCHAR(50) NOT NULL UNIQUE,
  correo VARCHAR(50) NULL UNIQUE
);

CREATE TABLE Turno (
  id_turno INT PRIMARY KEY,
  codigo_turno VARCHAR(50) NOT NULL UNIQUE,
  fecha DATE NOT NULL,
  hora_inicio TIME NOT NULL,
  hora_fin TIME NOT NULL
);

CREATE TABLE Reserva (
  id_reserva INT PRIMARY KEY,
  id_cliente INT NOT NULL,
  id_mesa INT NOT NULL,
  id_turno INT NOT NULL,
  fecha_reserva DATE NOT NULL,
  codigo_reserva VARCHAR(50) NOT NULL UNIQUE,
  estado VARCHAR(50) NOT NULL,
  FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
  FOREIGN KEY (id_mesa) REFERENCES Mesa(id_mesa),
  FOREIGN KEY (id_turno) REFERENCES Turno(id_turno)
);

CREATE TABLE Mesero (
  id_mesero INT PRIMARY KEY,
  codigo_mesero VARCHAR(50) NOT NULL UNIQUE,
  nombre VARCHAR(50) NOT NULL,
  telefono VARCHAR(50) NOT NULL,
  correo VARCHAR(50) NULL,
  id_jefe INT NULL,
  FOREIGN KEY (id_jefe) REFERENCES Mesero(id_mesero)
);

CREATE TABLE Pedido (
  id_pedido INT PRIMARY KEY,
  id_reserva INT NOT NULL,
  codigo_pedido VARCHAR(50) NOT NULL UNIQUE,
  fecha_pedido DATE NOT NULL,
  estado VARCHAR(50) NOT NULL,
  id_mesero INT NOT NULL,
  FOREIGN KEY (id_reserva) REFERENCES Reserva(id_reserva),
  FOREIGN KEY (id_mesero) REFERENCES Mesero(id_mesero)
);

CREATE TABLE DetallePedido (
  id_detalle INT PRIMARY KEY,
  id_pedido INT NOT NULL,
  id_plato INT NOT NULL,
  codigo_detallePedido VARCHAR(50) NOT NULL UNIQUE,
  cantidad INT NOT NULL,
  precio_unitario DECIMAL(10,4) NOT NULL,
  FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
  FOREIGN KEY (id_plato) REFERENCES Plato(id_plato)
);

CREATE TABLE Pago (
  id_pago INT PRIMARY KEY,
  codigo_pago VARCHAR(50) NOT NULL UNIQUE,
  id_pedido INT NOT NULL,
  fecha_pago DATE NOT NULL,
  monto DECIMAL(10,4) NOT NULL,
  metodo VARCHAR(50) NOT NULL,
  FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido)
);