class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    def navegar(self):
        self.page.goto("https://www.saucedemo.com/")

    def iniciar_sesion(self, usuario, contraseña):
        self.username_input.fill(usuario)
        self.password_input.fill(contraseña)
        self.login_button.click()

    def obtener_mensaje_error(self):
        return self.error_message.inner_text()
