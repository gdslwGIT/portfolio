from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.exit_intent_page import ExitIntentPage

def test_exit_intent_modal(page: Page, home: HomePage, exit_intent_page: ExitIntentPage):
    home.click_exit_intent()
    page.wait_for_url("**/exit-intent")
    page.wait_for_timeout(1000)
    expect(exit_intent_page.modal).not_to_have_class("modal fade show")
    page.mouse.move(100, 100)
    page.wait_for_timeout(500)
    page.mouse.move(100, -10)
    page.wait_for_timeout(1000)
    expect(exit_intent_page.modal).to_have_class("modal fade show")
    exit_intent_page.close_btn.click()
    page.wait_for_timeout(1000)
    expect(exit_intent_page.modal).not_to_have_class("modal fade show")
