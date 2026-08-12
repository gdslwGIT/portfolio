from playwright.sync_api import Page

class WindowsPage:
    def __init__(self, page: Page):
        self.page = page
        self.click_here_link = page.locator("a", has_text="Click Here")
