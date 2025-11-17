create database restaurante_db;
USE proyecto_final_restaurante;


CREATE TABLE CategoriaPlato (
  id_categoria INT PRIMARY KEY AUTO_INCREMENT,
  codigo_categoria VARCHAR(50) NOT NULL UNIQUE,
  nombre VARCHAR(50) NOT NULL
);


CREATE TABLE Plato (
  id_plato INT PRIMARY KEY AUTO_INCREMENT,
  codigo_plato VARCHAR(50) NOT NULL UNIQUE,
  nombre VARCHAR(50) NOT NULL,
  descripcion VARCHAR(100),
  precio DECIMAL(10,4) NOT NULL,
  id_categoria INT,
  FOREIGN KEY (id_categoria) REFERENCES CategoriaPlato(id_categoria)
);


CREATE TABLE Mesa (
  id_mesa INT PRIMARY KEY AUTO_INCREMENT,
  codigo_mesa VARCHAR(50) NOT NULL UNIQUE,
  capacidad INT NOT NULL DEFAULT 2
);

CREATE TABLE Cliente (
  id_cliente INT PRIMARY KEY AUTO_INCREMENT,
  codigo_cliente VARCHAR(50) NOT NULL UNIQUE,
  nombre VARCHAR(50) NOT NULL,
  telefono VARCHAR(50) NOT NULL UNIQUE,
  correo VARCHAR(50) UNIQUE
);


CREATE TABLE Turno (
  id_turno INT PRIMARY KEY AUTO_INCREMENT,
  codigo_turno VARCHAR(50) NOT NULL UNIQUE,
  fecha DATE NOT NULL DEFAULT (CURRENT_DATE),
  hora_inicio TIME NOT NULL,
  hora_fin TIME NOT NULL
);


CREATE TABLE Reserva (
  id_reserva INT PRIMARY KEY AUTO_INCREMENT,
  id_cliente INT NOT NULL,
  id_mesa INT NOT NULL,
  id_turno INT NOT NULL,
  fecha_reserva DATE NOT NULL DEFAULT (CURRENT_DATE),
  codigo_reserva VARCHAR(50) NOT NULL UNIQUE,
  estado VARCHAR(50) NOT NULL DEFAULT 'Pendiente',
  FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
  FOREIGN KEY (id_mesa) REFERENCES Mesa(id_mesa),
  FOREIGN KEY (id_turno) REFERENCES Turno(id_turno)
);


CREATE TABLE Mesero (
  id_mesero INT PRIMARY KEY AUTO_INCREMENT,
  codigo_mesero VARCHAR(50) NOT NULL UNIQUE,
  nombre VARCHAR(50) NOT NULL,
  telefono VARCHAR(50) NOT NULL,
  correo VARCHAR(50),
  id_jefe INT NULL,
  FOREIGN KEY (id_jefe) REFERENCES Mesero(id_mesero)
);


CREATE TABLE Pedido (
  id_pedido INT PRIMARY KEY AUTO_INCREMENT,
  id_reserva INT NOT NULL,
  codigo_pedido VARCHAR(50) NOT NULL UNIQUE,
  fecha_pedido DATE NOT NULL DEFAULT (CURRENT_DATE),
  estado VARCHAR(50) NOT NULL DEFAULT 'En proceso',
  id_mesero INT NOT NULL,
  FOREIGN KEY (id_reserva) REFERENCES Reserva(id_reserva),
  FOREIGN KEY (id_mesero) REFERENCES Mesero(id_mesero)
);


  id_detalle INT PRIMARY KEY AUTO_INCREMENT,
  id_pedido INT NOT NULL,
  id_plato INT NOT NULL,
  codigo_detallePedido VARCHAR(50) NOT NULL UNIQUE,
  cantidad INT NOT NULL DEFAULT 1,
  precio_unitario DECIMAL(10,4) NOT NULL,
  FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
  FOREIGN KEY (id_plato) REFERENCES Plato(id_plato)
);


CREATE TABLE Pago (
  id_pago INT PRIMARY KEY AUTO_INCREMENT,
  codigo_pago VARCHAR(50) NOT NULL UNIQUE,
  id_pedido INT NOT NULL,
  fecha_pago DATE NOT NULL DEFAULT (CURRENT_DATE),
  monto DECIMAL(10,4) NOT NULL,
  metodo VARCHAR(50) NOT NULL DEFAULT 'Efectivo',
  FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido)
);

CREATE TABLE MeseroPedido (
  id_mesero INT NOT NULL,
  id_pedido INT NOT NULL,
  rol VARCHAR(50) NOT NULL DEFAULT 'Asistente',
  PRIMARY KEY (id_mesero, id_pedido),
  FOREIGN KEY (id_mesero) REFERENCES Mesero(id_mesero),
  FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido)
);

SELCET *FROM  Pedido;
