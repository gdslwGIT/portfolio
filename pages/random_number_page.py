from playwright.sync_api import Page

class RandomNumberPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.header = page.locator("h1")
        self.random_number_box = page.locator("#randomNumber")
        
    def get_number_value(self) -> float:
        text = self.random_number_box.inner_text().strip()
        return float(text)
