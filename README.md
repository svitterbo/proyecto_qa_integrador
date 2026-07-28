# Proyecto QA Integrador — E-Commerce

![QA Suite](https://github.com/svitterbo/proyecto_qa_integrador/actions/workflows/qa_suite.yml/badge.svg)

## Objetivo

Este proyecto integra las 3 capas clásicas de una pirámide de testing sobre un mismo dominio simulado de e-commerce, demostrando cómo se complementan en un flujo real de QA:

- **Base de datos** — integridad de datos y reglas de negocio a nivel de esquema
- **API** — contratos de endpoints, status codes y validación de estructura de respuesta
- **UI (E2E)** — flujos de usuario reales de punta a punta, con Page Object Model

Las 3 capas corren de forma automática en cada push mediante un pipeline de CI con GitHub Actions.

## Arquitectura

proyecto_qa_integrador/
├── .github/workflows/qa_suite.yml # Pipeline de CI (3 jobs en paralelo)
├── tests_db/ # Tests de integridad de datos (Pytest + psycopg2)
│ ├── conftest.py # Fixture de conexión a Postgres
│ └── test_integridad.py
├── tests_api/ # Tests de API (Pytest + requests + jsonschema)
│ └── test_endpoints.py
├── tests_e2e/ # Tests E2E (Pytest + Playwright + POM)
│ ├── pages/ # Page Objects
│ │ ├── login_page.py
│ │ ├── inventory_page.py
│ │ └── checkout_page.py
│ ├── test_login.py
│ ├── test_carrito.py
│ └── test_checkout.py
├── setup_datos.sql # Carga de datos de prueba para Postgres
└── requirements.txt

## Stack

| Capa | Herramientas |
|---|---|
| DB | PostgreSQL, psycopg2, Pytest |
| API | requests, jsonschema, Pytest (contra [JSONPlaceholder](https://jsonplaceholder.typicode.com)) |
| E2E | Playwright, Pytest, Page Object Model, pytest-html (contra [SauceDemo](https://www.saucedemo.com)) |
| CI/CD | GitHub Actions, con Postgres corriendo como *service container* |

## Cómo correrlo localmente

### 1. Clonar y crear el entorno virtual

```bash
git clone https://github.com/svitterbo/proyecto_qa_integrador.git
cd proyecto_qa_integrador
python3 -m venv venv
source venv/bin/activate     # o venv/bin/activate.fish si usás fish
pip install -r requirements.txt
playwright install --with-deps chromium
```

### 2. Levantar Postgres y cargar datos de prueba

Con Postgres corriendo localmente, creá el usuario y la base:

```sql
CREATE USER testuser WITH PASSWORD 'testpass';
CREATE DATABASE ecommerce_test OWNER testuser;
```

Cargá el esquema y los datos:

```bash
PGPASSWORD=testpass psql -h localhost -U testuser -d ecommerce_test -f setup_datos.sql
```

### 3. Correr toda la suite

```bash
pytest -v                    # todo junto
pytest tests_db/ -v          # solo la capa de DB
pytest tests_api/ -v         # solo la capa de API
pytest tests_e2e/ -v         # solo la capa E2E
```

## CI/CD

El workflow `.github/workflows/qa_suite.yml` corre automáticamente en cada `push` y `pull_request` a `main`, ejecutando las 3 suites en jobs paralelos. La capa de DB usa un **service container** de Postgres, levantado por GitHub Actions únicamente para la duración del job — sin necesidad de infraestructura externa.

## Origen del proyecto

Este integrador combina y reestructura 3 proyectos previos del mismo autor:
- [proyecto_sql_testing](https://github.com/svitterbo/proyecto_sql_testing)
- [proyecto_api](https://github.com/svitterbo/proyecto_api)
- [proyecto_saucedemo](https://github.com/svitterbo/proyecto_saucedemo)
