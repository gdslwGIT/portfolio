from playwright.sync_api import Page

class FeedbackPage:
    def __init__(self, page: Page):
        self.page = page
        self.contact_header = page.locator("a[href='#panel1']")
        self.name_input = page.locator("#yourName")
        self.email_input = page.locator("#yourEmail")
        self.message_input = page.locator("div.content[data-slug='panel1'] textarea")
        self.submit_btn = page.locator("div.content[data-slug='panel1'] button")
