from playwright.sync_api import Page

from tests_e2e.pages.checkout_page import CheckoutPage
from tests_e2e.pages.inventory_page import InventoryPage
from tests_e2e.pages.login_page import LoginPage


def test_flujo_compra_completo(page: Page):
    login_page = LoginPage(page)
    login_page.navegar()
    login_page.iniciar_sesion("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.agregar_mochila()

    checkout_page = CheckoutPage(page)
    checkout_page.ir_al_carrito_y_comprar()
    checkout_page.llenar_datos_envio("Santiago", "Vitterbo", "6000")
    checkout_page.finalizar_compra()

    assert checkout_page.obtener_mensaje_confirmacion() == "Thank you for your order!"
