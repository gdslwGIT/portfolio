from playwright.sync_api import Page, Locator

class ShouldHavePage:
    def __init__(self, page: Page):
        self.page = page
        self.header = page.locator("h1")
        self.description = page.locator("p").first
        self.btn1 = page.locator("#btn1, button:has-text('btn1')").first
        self.btn2 = page.locator("#btn2, button:has-text('btn2')").first
        self.div1 = page.locator("#div1, [id*='div1']").first
        self.div1_text = page.get_by_text("Div has css applied")
        self.list_items = page.locator("#ul1 li, main ul li")
        self.input1 = page.locator("#input1, input").first
