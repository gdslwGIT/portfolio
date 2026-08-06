from playwright.sync_api import Page

class RedirectorPage:
    def __init__(self, page: Page):
        self.page = page
        self.redirect_link = page.locator("#redirect")
        self.status_codes_header = page.locator(".page-layout h1")
