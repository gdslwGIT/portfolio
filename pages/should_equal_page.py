from playwright.sync_api import Page, Locator

class ShouldEqualPage:
    def __init__(self, page: Page):
        self.page = page
        self.header = page.locator("h1")
        self.description = page.locator("p:has-text('should equal')")
        self.equal_text = page.get_by_text("'equal'")
        self.input1_heading = page.locator("h6:has-text('input1')")
        self.simple_div = page.get_by_text("A simple div")
