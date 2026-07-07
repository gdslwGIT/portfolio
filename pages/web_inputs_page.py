from playwright.sync_api import Page


class WebInputsPage:
    def __init__(self, page: Page):
        self.page = page