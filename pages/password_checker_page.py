from playwright.sync_api import Page

class PasswordCheckerPage:
    def __init__(self, page: Page):
        self.page = page
        self.password_input = page.locator(".password")
        self.length_rule = page.locator(".helper-text .length")
        self.lowercase_rule = page.locator(".helper-text .lowercase")
        self.uppercase_rule = page.locator(".helper-text .uppercase")
        self.special_rule = page.locator(".helper-text .special")

    def enter_password(self, password: str):
        self.password_input.fill(password)
        self.password_input.press("End")
