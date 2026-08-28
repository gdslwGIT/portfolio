from playwright.sync_api import Page

class HttpHeadersPage:
    def __init__(self, page: Page):
        self.page = page
        self.header = page.locator("h1")
        
    def get_header_value(self, header_name: str):
        return self.page.locator(f"xpath=//table//tr[td[text()='{header_name.lower()}']]/td[2]")
