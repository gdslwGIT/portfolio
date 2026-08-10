from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.floating_menu_page import FloatingMenuPage

def test_floating_menu(page: Page, home: HomePage, floating_menu_page: FloatingMenuPage):
    home.click_floating_menu()
    page.wait_for_url("**/floating-menu")
    page.wait_for_timeout(1000)

    expect(floating_menu_page.menu).to_be_in_viewport()

    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(1000)

    expect(floating_menu_page.menu).to_be_in_viewport()
