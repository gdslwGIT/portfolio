from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.key_presses_page import KeyPressesPage

def test_key_presses(page: Page, home: HomePage, key_presses_page: KeyPressesPage):
    home.click_key_presses()
    page.wait_for_url("**/key-presses")
    page.wait_for_timeout(1000)

    key_presses_page.target_input.click()

    key_presses_page.target_input.press("Space")
    expect(key_presses_page.result).to_have_text("You entered: SPACE")
    page.wait_for_timeout(1000)

    key_presses_page.target_input.press("Escape")
    expect(key_presses_page.result).to_have_text("You entered: ESCAPE")
    page.wait_for_timeout(1000)

    key_presses_page.target_input.press("a")
    expect(key_presses_page.result).to_have_text("You entered: A")
    page.wait_for_timeout(1000)

    

    