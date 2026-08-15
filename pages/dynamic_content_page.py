from playwright.sync_api import Page

class DynamicContentPage:
    def __init__(self, page: Page):
        self.page = page

        self.row1_img = page.locator("#content > .row img").nth(0)
        self.row1_txt = page.locator("#content > .row > .col-md-10").nth(0)

        self.row2_img = page.locator("#content > .row img").nth(1)
        self.row2_txt = page.locator("#content > .row > .col-md-10").nth(1)

        self.row3_img = page.locator("#content > .row img").nth(2)
        self.row3_txt = page.locator("#content > .row > .col-md-10").nth(2)

    
    