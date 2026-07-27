"""
Suite de tests de integridad de datos.
Migrado desde proyecto_sql_testing/validaciones_db.sql
Cada query original devolvía 0 filas si todo estaba OK;
acá esa misma lógica se convierte en un assert.
"""


def test_no_hay_emails_duplicados(db_cursor):
    """
    TEST CASE 1 (original): usuarios con el mismo email repetido.
    Esperado: 0 filas -> ningún email debe repetirse.
    """
    db_cursor.execute("""
        SELECT email, COUNT(*) as cantidad_duplicados
        FROM usuarios
        GROUP BY email
        HAVING COUNT(*) > 1;
    """)
    duplicados = db_cursor.fetchall()

    assert duplicados == [], f"Se encontraron emails duplicados: {duplicados}"


def test_emails_tienen_formato_valido(db_cursor):
    """
    TEST CASE 2 (original): emails que no cumplen el patrón básico usuario@dominio.
    Esperado: 0 filas -> todos los emails están bien formateados.
    """
    db_cursor.execute("""
        SELECT usuario_id, email
        FROM usuarios
        WHERE email NOT LIKE '%@%.%';
    """)
    emails_invalidos = db_cursor.fetchall()

    assert emails_invalidos == [], f"Emails con formato inválido: {emails_invalidos}"


def test_compras_huerfanas(db_cursor):
    """
    TEST CASE 3 (original): verificar que las compras se realicen por usuarios registrados.
    Esperado: 0 filas -> todos las compras hechas por usuarios registrados.
    """

    db_cursor.execute("""
        SELECT c.compra_id, c.usuario_id
        FROM compras c
        LEFT JOIN usuarios u ON c.usuario_id = u.usuario_id
        WHERE u.usuario_id IS NULL;
        """)
    compras_huerfanas = db_cursor.fetchall()

    assert compras_huerfanas == [], f"Compras de usuarios sin id: {compras_huerfanas}"


def test_precio_stock_invalidos(db_cursor):
    """
    TEST CASE 4 (original): verificar que el precio y el stock sean distintos a 0.
    Esperado: 0 filas -> precios correctos y stock disponible.
    """

    db_cursor.execute("""
        SELECT producto_id, nombre, precio, stock
        FROM productos
        WHERE precio <= 0 OR stock < 0;
        """)
    stock_precio = db_cursor.fetchall()

    assert stock_precio == [], f"Stock o precios invalidos: {stock_precio}"


def test_ordenes_completadas_sin_fecha_entrega(db_cursor):
    """
    TEST CASE 5 (original): Ordenes de compras que no tengan su fecha de entrega.
    Esperado: 0 filas -> todas las ordenes de compras cuentan con fecha de entrega.
    """

    db_cursor.execute("""
        SELECT compra_id, estado, fecha_entrega
        FROM compras
        WHERE estado = 'Completado' AND fecha_entrega IS NULL;
        """)
    ordenes_compras = db_cursor.fetchall()

    assert ordenes_compras == [], (
        f"Las ordenes de compras sin fecha de entrega son: {ordenes_compras}"
    )
