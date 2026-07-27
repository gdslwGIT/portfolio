from playwright.sync_api import Page

class InfiniteScrollPage:
    def __init__(self, page: Page):
        self.page = page
        self.scroll_items = page.locator(".scroll b")

    def scroll_down(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
        