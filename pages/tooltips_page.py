from playwright.sync_api import Page

class TooltipsPage:
    def __init__(self, page: Page):
        self.page = page
        self.btn1 = page.locator("#btn1")
        self.btn2 = page.locator("#btn2")
        self.btn3 = page.locator("#btn3")
        self.btn4 = page.locator("#btn4")
        self.btn5 = page.locator("#btn5")
        self.tooltip_inner = page.locator(".tooltip-inner")