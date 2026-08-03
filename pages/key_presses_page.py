from playwright.sync_api import Page

class KeyPressesPage:
    def __init__(self, page: Page):
        self.page = page
        self.target_input = page.locator("#target")
        self.result = page.locator("#result")
