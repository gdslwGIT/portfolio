from playwright.sync_api import Page

class JsDialogsPage:
    def __init__(self, page: Page):
        self.page = page
        self.alert_button = page.locator("#js-alert")
        self.confirm_button = page.locator("#js-confirm")
        self.prompt_button = page.locator("#js-prompt")
        self.response = page.locator("#dialog-response")

    
        