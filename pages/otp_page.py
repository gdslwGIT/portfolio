from playwright.sync_api import Page

class OtpPage:
    def __init__ (self, page: Page):
        self.page = page
        self.email_input = page.locator("#email")
        self.send_otp_button = page.locator("#btn-send-otp")
        self.otp_message = page.locator("#otp-message")
        self.otp_input = page.locator("#otp")
        self.verify_button = page.locator("#btn-send-verify")

    def send_otp(self, email: str):
        self.email_input.fill(email)
        self.send_otp_button.click()

    def verify_otp(self, otp_code: str):
        self.otp_input.fill(otp_code)
        self.verify_button.click()