from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.autocomplete_page import AutoCompletePage

def test_autocomplete(page: Page, home: HomePage, autocomplete_page: AutoCompletePage):
    home.click_autocomplete()
    page.wait_for_url("**/autocomplete")
    page.wait_for_timeout(1000)
    autocomplete_page.type_country("Sw")
    page.wait_for_timeout(1000)
    autocomplete_page.select_suggestion("Switzerland")
    page.wait_for_timeout(1000)
    autocomplete_page.click_submit()
    page.wait_for_timeout(1000)
    expect(autocomplete_page.result_message).to_have_text("You selected: Switzerland")
