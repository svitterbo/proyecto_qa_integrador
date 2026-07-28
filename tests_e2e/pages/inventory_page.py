class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.btn_agregar_mochila = page.locator(
            "[data-test='add-to-cart-sauce-labs-backpack']"
        )
        self.icono_carrito = page.locator(".shopping_cart_badge")

    def agregar_mochila(self):
        self.btn_agregar_mochila.click()

    def obtener_cantidad_carrito(self):
        return self.icono_carrito.inner_text()
