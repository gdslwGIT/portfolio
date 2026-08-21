from playwright.sync_api import Page

class ExitIntentPage:
    def __init__(self, page: Page):
        self.page = page
        self.modal = page.locator("#exampleModal")
        self.close_btn = page.locator("#close-modal-btn")
