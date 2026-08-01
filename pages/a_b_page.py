from playwright.sync_api import Page


class ABPage:
    def __init__ (self, page: Page):
        self.page = page
        self.header = page.locator(".page-layout h1")