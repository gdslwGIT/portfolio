from playwright.sync_api import Page , expect
from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_successful_login_and_logout(home:HomePage, login_page: LoginPage, page: Page):
    home.click_login_page()
    page.wait_for_url("**/login")
    login_page.login("practice", "SuperSecretPassword!")
    page.wait_for_url("**/secure")
    login_page.logout()
    page.wait_for_url("**/login")

def test_invalid_password(home: HomePage, page: Page, login_page: LoginPage):
    home.click_login_page()
    page.wait_for_url("**/login")
    login_page.login("practice", "WrongPassword!")
    expect(login_page.flash_message).to_contain_text("Your password is invalid!")
