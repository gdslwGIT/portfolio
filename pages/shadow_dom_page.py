from playwright.sync_api import Page 

class ShadowDomPage:
    def __init__(self, page: Page):
        self.page = page
        self.normal_button = page.locator("button#my-btn").first
        self.shadow_button = page.locator("#shadow-host #my-btn")
        
    