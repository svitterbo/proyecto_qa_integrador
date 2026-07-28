"""
Suite de tests de API.
Migrado desde proyecto_api/test_api.py
Apunta a JSONPlaceholder (https://jsonplaceholder.typicode.com),
una API pública de prueba - no requiere levantar ningún servidor local.
"""

import requests
from jsonschema import validate

BASE_URL = "https://jsonplaceholder.typicode.com"

SCHEMA_USUARIO = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string"},
    },
    "required": ["id", "name", "email"],
}


def test_obtener_usuario_existente_y_validar_esquema():
    """
    Happy path: GET a un usuario que existe.
    Valida status code, un dato puntual del payload, y el schema completo.
    """
    respuesta = requests.get(f"{BASE_URL}/users/1")
    assert respuesta.status_code == 200

    datos = respuesta.json()
    assert datos["name"] == "Leanne Graham"

    validate(instance=datos, schema=SCHEMA_USUARIO)


def test_usuario_no_encontrado():
    """
    Sad path: GET a un usuario que no existe.
    El servidor debe responder 404, no un 200 con datos vacíos ni un 500.
    """
    respuesta = requests.get(f"{BASE_URL}/users/999")
    assert respuesta.status_code == 404
