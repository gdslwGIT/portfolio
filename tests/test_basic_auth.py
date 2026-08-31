from playwright.sync_api import Page, expect, Error
from pages.home_page import HomePage
from pages.basic_authentication_page import BasicAuthenticationPage

def test_basic_auth_success(page: Page, home: HomePage, basic_authentication_page: BasicAuthenticationPage):
    home.click_basic_authentication()
    page.wait_for_url("**/basic-auth")
    page.wait_for_timeout(1000)
    
    expect(basic_authentication_page.header).to_have_text("Basic Auth page for Automation Testing Practice")
    
    expect(basic_authentication_page.alert_success).to_be_visible()
    expect(basic_authentication_page.alert_success).to_contain_text("Congratulations! You must have the proper credentials.")

def test_basic_auth_unauthorized(browser):
    context = browser.new_context()
    page = context.new_page()
    try:
        page.goto("https://practice.expandtesting.com/basic-auth")
        assert False, "Expected ERR_INVALID_AUTH_CREDENTIALS error, but page loaded successfully"
    except Error as e:
        assert "net::ERR_INVALID_AUTH_CREDENTIALS" in str(e)

    context.close()
