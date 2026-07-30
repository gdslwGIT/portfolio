from playwright.sync_api import Page 

class JsErrorPage:
    def __init__(self, page: Page):
        self.page = page
