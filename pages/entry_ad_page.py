from playwright.sync_api import Page

class EntryAdPage:
    def __init__(self, page: Page):
        self.page = page
        self.modal = page.locator("#exampleModal")
        self.close_btn = page.locator("#close-modal-btn")
        self.restart_link = page.locator("#restart-ad")
