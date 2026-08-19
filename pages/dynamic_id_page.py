from playwright.sync_api import Page

class DynamicIdPage:
    def __init__(self, page: Page):
        self.page = page

        self.dynamic_btn = page.locator("button:has-text('Button with Dynamic ID')")
