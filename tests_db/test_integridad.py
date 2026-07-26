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
