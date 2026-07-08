from playwright.sync_api import Page , expect
from pages.home_page import HomePage
from pages.register_page import RegisterPage

def test_successful_registration(home: HomePage, page: Page, login_page: LoginPage, register_page: RegisterPage, faker):
    home.click_register_page()
    page.wait_for_url("**/register")
    username = faker.user_name()
    password = faker.password()
    register_page.register(username, password)
    page.wait_for_url("**/login")
    login_page.login(username, password)
    page.wait_for_url("**/secure")

def test_unsuccessful_registration(home:HomePage, page: Page, register_page: RegisterPage):
    home.click_register_page()
    page.wait_for_url("**/register")
    register_page.register("Test", "Test")
    expect(register_page.flash_message).to_contain_text("An error occurred during registration. Please try again.")
    