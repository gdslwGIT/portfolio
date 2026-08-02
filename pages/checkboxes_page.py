from playwright.sync_api import Page 


class CheckBoxPage:
    def __init__(self , page: Page):
        self.page = page
        self.checkbox1 = page.locator("#checkbox1")
        self.checkbox2 = page.locator("#checkbox2")