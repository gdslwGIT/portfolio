from playwright.sync_api import Page

class ScrollbarsPage:
    def __init__(self, page: Page):
        self.page = page
        self.hiding_button = page.locator("#hidingButton")
