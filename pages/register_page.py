from playwright.sync_api import Page

class RegisterPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.password_confirm_input = page.locator("#confirmPassword")
        self.register_button = page.locator('button[type="submit"]')
        self.flash_message = page.locator("#flash")
        
    def register(self, username:str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.password_confirm_input.fill(password)
        self.register_button.click()
        
    