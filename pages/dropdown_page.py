from playwright.sync_api import Page


class DropdownPage:
    def __init__(self, page: Page):
        self.page = page
        self.simple_dropdown = page.locator("#dropdown")
        self.elements_dropdown = page.locator("#elementsPerPageSelect")
        self.country_dropdown = page.locator("#country")