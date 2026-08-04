from playwright.sync_api import Page

class DissapearingElementsPage:
    def __init__(self, page: Page):
        self.page = page
        self.buttons = page.locator(".page-layout button")
        self.starred_button = page.locator("button:has-text('Starred')")