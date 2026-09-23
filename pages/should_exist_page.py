from playwright.sync_api import Page, Locator

class ShouldExistPage:
    def __init__(self, page: Page):
        self.page = page
        self.header = page.locator("h1")
        self.description = page.locator("p:has-text('should exist')")
        self.input1_heading = page.locator("h6:has-text('input1')")
