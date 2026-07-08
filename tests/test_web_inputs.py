from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.web_inputs_page import WebInputsPage

def test_web_inputs(home: HomePage, page: Page, web_inputs: WebInputsPage):
    home.click_web_inputs()
    page.wait_for_url("**/inputs")
    web_inputs.fill_form("123", "Hello World", "12345QWERTY", "2000-12-12")
    web_inputs.click_display_inputs()
    expect(web_inputs.check_input_number).to_have_text("123")
    expect(web_inputs.check_input_text).to_have_text("Hello World")
    expect(web_inputs.check_input_password).to_have_text("12345QWERTY")
    expect(web_inputs.check_input_date).to_have_text("2000-12-12")