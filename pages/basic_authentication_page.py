from playwright.sync_api import Page

class BasicAuthenticationPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.header = page.locator("h1")
        self.alert_success = page.locator("p.alert-success")
