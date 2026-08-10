from playwright.sync_api import Page

class FloatingMenuPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu = page.locator("#menu")
