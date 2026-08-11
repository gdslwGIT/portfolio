from playwright.sync_api import Page

class IFramePage:
    def __init__(self, page: Page):
        self.page = page
        self.subscribe_iframe = page.frame_locator("#email-subscribe")
        self.email_input = self.subscribe_iframe.locator("#email")
        self.subscribe_button = self.subscribe_iframe.locator("#btn-subscribe")
        self.success_message = self.subscribe_iframe.locator("#success-message")
