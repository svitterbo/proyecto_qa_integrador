from playwright.sync_api import Page

from tests_e2e.pages.login_page import LoginPage


def test_login_exitoso(page: Page):
    login_page = LoginPage(page)
    login_page.navegar()
    login_page.iniciar_sesion("standard_user", "secret_sauce")

    assert page.url == "https://www.saucedemo.com/inventory.html"


def test_login_fallido(page: Page):
    login_page = LoginPage(page)
    login_page.navegar()

    login_page.iniciar_sesion("standard_user", "clave_falsa_123")

    mensaje_esperado = (
        "Epic sadface: Username and password do not match any user in this service"
    )
    assert login_page.obtener_mensaje_error() == mensaje_esperado
