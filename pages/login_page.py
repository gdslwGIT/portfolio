from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#submit-login")
        self.logout_button = page.locator('a[href="/logout"]')
        self.flash_message = page.locator("#flash")

    def login(self, username: str, password:str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
    
    def logout(self):
        self.logout_button.click()