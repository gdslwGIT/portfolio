from playwright.sync_api import Page

class ContactPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.name_input = page.locator("div.mb-3:has(label:has-text('Name')) input")
        self.email_input = page.locator("div.mb-3:has(label:has-text('Email')) input")
        self.message_input = page.locator("div.mb-3:has(label:has-text('You message')) textarea")
        
        self.send_btn = page.get_by_role("link", name="Send")
