from playwright.sync_api import Page

class CookieAlertPage:
    def __init__(self, page: Page):
        self.page = page
        self.cookie_box = page.locator("#js-cookie-box")
        self.accept_btn = page.locator("#js-cookie-button")
