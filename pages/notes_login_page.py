from playwright.sync_api import Page

class NotesLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.header = page.locator("h1")
        self.email_input = page.locator("[data-testid='login-email']")
        self.password_input = page.locator("[data-testid='login-password']")
        self.submit_btn = page.locator("[data-testid='login-submit']")
        self.alert_message = page.locator("[data-testid='alert-message']")
        self.forgot_password_link = page.locator("#forgotPasswordLink")
        self.google_login_btn = page.locator("[data-testid='login-with-google']")
        self.linkedin_login_btn = page.locator("[data-testid='login-with-linkedin']")
        self.register_link = page.locator("a:has-text('Create a free account!')")
