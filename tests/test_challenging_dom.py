from playwright.sync_api import Page , expect
from pages.home_page import HomePage
from pages.challenging_dom_page import ChallengingDomPage

def test_challenging_dom(page: Page, home: HomePage, challenging_dom_page: ChallengingDomPage):
    home.click_challenging_dom()
    page.wait_for_url("**/challenging-dom")
    page.wait_for_timeout(1000)
    challenging_dom_page.blue_button.click()
    challenging_dom_page.warning_button.click()
    challenging_dom_page.success_button.click()
    page.wait_for_timeout(1000)
    challenging_dom_page.click_delete_for_row("Iuvaret2")
    page.wait_for_timeout(1000)
    assert page.url.endswith("#delete")
    challenging_dom_page.click_edit_for_row("Iuvaret4")
    page.wait_for_timeout(1000)
    assert page.url.endswith("#edit")