class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.cart_link = page.locator(".shopping_cart_link")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input = page.locator("[data-test='lastName']")
        self.postal_code_input = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")
        self.complete_header = page.locator(".complete-header")

    def ir_al_carrito_y_comprar(self):
        self.cart_link.click()
        self.checkout_button.click()

    def llenar_datos_envio(self, nombre, apellido, codigo_postal):
        self.first_name_input.fill(nombre)
        self.last_name_input.fill(apellido)
        self.postal_code_input.fill(codigo_postal)
        self.continue_button.click()

    def finalizar_compra(self):
        self.finish_button.click()

    def obtener_mensaje_confirmacion(self):
        return self.complete_header.inner_text()
