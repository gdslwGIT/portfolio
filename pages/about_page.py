from playwright.sync_api import Page

class AboutPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.header = page.locator("h1")
        self.welcome_heading = page.locator("h2", has_text="Welcome to our Practice WebApp!")
        self.contact_email_link = page.locator('a[href="mailto:expand.testing@gmail.com"]')
