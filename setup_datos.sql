-- ============================================================================
-- SETUP: Creación de tablas y carga de datos de prueba (versión "limpia")
-- Todos los datos cumplen las reglas de negocio -> la suite de tests_db
-- debe pasar en verde, demostrando un pipeline de integridad funcionando.
-- ============================================================================

DROP TABLE IF EXISTS compras;
DROP TABLE IF EXISTS productos;
DROP TABLE IF EXISTS usuarios;

CREATE TABLE usuarios (
    usuario_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE productos (
    producto_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio NUMERIC(10, 2) NOT NULL,
    stock INTEGER NOT NULL
);

CREATE TABLE compras (
    compra_id SERIAL PRIMARY KEY,
    usuario_id INTEGER,
    estado VARCHAR(20) NOT NULL,
    fecha_entrega DATE
);

-- Usuarios: emails únicos y bien formateados
INSERT INTO usuarios (nombre, email) VALUES
    ('Ana Gomez', 'ana.gomez@mail.com'),
    ('Pedro Diaz', 'pedro.diaz@mail.com'),
    ('Lucia Fernandez', 'lucia.fernandez@mail.com'),
    ('Martin Rojas', 'martin.rojas@mail.com');

-- Productos: precios > 0 y stock >= 0
INSERT INTO productos (nombre, precio, stock) VALUES
    ('Teclado mecánico', 45000.00, 20),
    ('Mouse inalámbrico', 8000.00, 15),
    ('Monitor 24"', 120000.00, 3),
    ('Auriculares', 25000.00, 8);

-- Compras: todas con usuario_id válido, y las "Completadas" con fecha
INSERT INTO compras (usuario_id, estado, fecha_entrega) VALUES
    (1, 'Completado', '2026-06-15'),
    (2, 'Pendiente', NULL),
    (3, 'Completado', '2026-06-20'),
    (4, 'Completado', '2026-07-01');
