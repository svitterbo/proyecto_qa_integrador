import os

import psycopg2
import pytest


@pytest.fixture(scope="session")
def db_connection():
    """
    Abre una conexión a Postgres una sola vez por sesión de tests
    (no en cada test individual, sería un desperdicio de recursos).
    Los valores por defecto sirven para correrlo en tu compu local;
    en GitHub Actions, las env vars del workflow los sobreescriben.
    """
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "testuser"),
        password=os.getenv("DB_PASSWORD", "testpass"),
        dbname=os.getenv("DB_NAME", "ecommerce_test"),
        port=5432,
    )
    yield conn
    conn.close()


@pytest.fixture
def db_cursor(db_connection):
    """
    Da un cursor nuevo por cada test individual.
    Así un test no queda 'contaminado' por queries de otro test.
    """
    cursor = db_connection.cursor()
    yield cursor
    cursor.close()
