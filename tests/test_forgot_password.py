from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.forgot_password_page import ForgotPasswordPage

def test_forgot_password(page: Page, home: HomePage, forgot_password_page: ForgotPasswordPage, mailbox):
    home.click_forgot_password()
    page.wait_for_url("**/forgot-password")
    forgot_password_page.retrieve_password(mailbox.email)
    page.wait_for_timeout(5000)
    emails = mailbox.wait_for_mail(timeout=15)
    email_id = emails[0]["mail_id"]
    mail_body = mailbox.get_mail_body(email_id)
    assert "A forgot password retrieval was initiated" in mail_body