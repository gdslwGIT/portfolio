from playwright.sync_api import Page, Locator

class MochawesomeReportsPage:
    def __init__(self, page: Page):
        self.page = page
        self.header = page.locator("h1")
        self.report_heading = page.locator("h2, h3, a:has-text('Report #1'), :text('Report #1')").first
