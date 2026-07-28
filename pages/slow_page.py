from playwright.sync_api import Page

class SlowPage:
    def __init__(self, page: Page):
        self.page = page
        self.result_message = page.locator("#result p")