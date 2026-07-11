import re
from playwright.sync_api import Page , expect
from pages.home_page import HomePage
from pages.otp_page import OtpPage

def test_otp_login(page: Page, home: HomePage, otp_page: OtpPage, mailbox):
    home.click_otp_login()
    page.wait_for_url("**/otp-login")
    otp_page.send_otp(mailbox.email)
    emails = mailbox.wait_for_mail()
    new_email = [m for m in emails if m['mail_id'] != '1'][0]
    email_body = mailbox.get_mail_body(new_email['mail_id'])
    otp_code = re.search(r"Your OTP code is (\d{6})", email_body).group(1)
    otp_page.verify_otp(otp_code)
    page.wait_for_url("**/secure")

def test_invalid_otp_login(page: Page, home: HomePage, otp_page: OtpPage, mailbox):
    home.click_otp_login()
    page.wait_for_url("**/otp-login")
    otp_page.send_otp(mailbox.email)
    otp_page.verify_otp("111111")
    expect(otp_page.otp_message).to_have_text("The provided OTP code is incorrect. Please check your code and try again.")