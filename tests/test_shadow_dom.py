from playwright.sync_api import Page , expect
from pages.home_page import HomePage
from pages.shadow_dom_page import ShadowDomPage

def test_shadow_dom(page: Page, home: HomePage, shadow_dom_page: ShadowDomPage):
    home.click_shadow_dom()
    page.wait_for_url("**/shadowdom")
    page.wait_for_timeout(1000)
    expect(shadow_dom_page.normal_button).to_have_text("Here's a basic button example.")
    expect(shadow_dom_page.shadow_button).to_have_text("This button is inside a Shadow DOM.")
    shadow_dom_page.normal_button.click()
    shadow_dom_page.shadow_button.click()
    page.wait_for_timeout(1000)

