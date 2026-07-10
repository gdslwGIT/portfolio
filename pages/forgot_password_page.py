from playwright.sync_api import Page

class ForgotPasswordPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_form = page.locator("#email")
        self.retrive_password_button = page.locator("button[type='submit']")

    def retrieve_password(self, email):
        self.email_form.fill(email)
        self.retrive_password_button.click()

