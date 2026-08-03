from playwright.sync_api import Page

class ContextMenuPage:
    def __init__(self, page: Page):
        self.page = page
        self.context_menu = page.locator("#hot-spot")

    def right_click(self):
        self.context_menu.dispatch_event("contextmenu")
