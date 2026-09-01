from playwright.sync_api import Page, expect, Error
from pages.home_page import HomePage
from pages.digest_authentication_page import DigestAuthenticationPage

def test_digest_auth_success(page: Page, home: HomePage, digest_authentication_page: DigestAuthenticationPage):
    home.click_digest_authentication()
    page.wait_for_url("**/digest-auth")
    page.wait_for_timeout(1000)
    
    expect(digest_authentication_page.header).to_have_text("Digest Auth page for Automation Testing Practice")
    expect(digest_authentication_page.alert_success).to_be_visible()
    expect(digest_authentication_page.alert_success).to_contain_text("Congratulations! You must have the proper credentials.")

def test_digest_auth_unauthorized(browser):
    context = browser.new_context()
    page = context.new_page()
    try:
        page.goto("https://practice.expandtesting.com/digest-auth")
        assert False, "Expected ERR_INVALID_AUTH_CREDENTIALS error, but page loaded successfully"
    except Error as e:
        assert "net::ERR_INVALID_AUTH_CREDENTIALS" in str(e)

    context.close()
