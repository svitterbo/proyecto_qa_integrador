from playwright.sync_api import Page

from tests_e2e.pages.inventory_page import InventoryPage
from tests_e2e.pages.login_page import LoginPage


def test_agregar_producto_al_carrito(page: Page):
    login_page = LoginPage(page)
    login_page.navegar()
    login_page.iniciar_sesion("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.agregar_mochila()

    assert inventory_page.obtener_cantidad_carrito() == "1"
