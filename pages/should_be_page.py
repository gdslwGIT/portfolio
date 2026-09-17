from playwright.sync_api import Page, Locator

class ShouldBePage:
    def __init__(self, page: Page):
        self.page = page
        self.header = page.locator("h1")
        self.description = page.locator("p").first
        self.list_items = page.locator("main ul li")
        self.div1_heading = page.locator("h6:has-text('div1')")
        self.div2_heading = page.locator("h6:has-text('div2')")
        self.div2_text = page.get_by_text("Text for div2")

    def get_list_items_count(self) -> int:
        return self.list_items.count()

    def get_list_item_text(self, index: int) -> str:
        return self.list_items.nth(index).inner_text()
