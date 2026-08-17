from playwright.sync_api import Page

class DynamicLoadingPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.example1_link = page.locator("a[href='/dynamic-loading/1']")
        self.example2_link = page.locator("a[href='/dynamic-loading/2']")
        
        self.start_btn = page.locator("#start button")
        self.loading = page.locator("#loading")
        self.finish_text = page.locator("#finish h4")
