from playwright.sync_api import Page

class DynamicControlsPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.checkbox = page.locator("#checkbox-example input")
        self.checkbox_btn = page.locator("#checkbox-example button")
        
        self.input_field = page.locator("#input-example input")
        self.input_btn = page.locator("#input-example button")
        
        self.loading = page.locator("#loading:visible")
        self.message = page.locator("#message")
