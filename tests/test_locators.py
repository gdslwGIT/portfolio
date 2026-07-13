from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.locators_page import LocatorsPage

def test_locators(page: Page, home: HomePage, locators_page: LocatorsPage):
    home.click_locators()
    page.wait_for_url("**/locators")
    locators_page.click_contact()
    page.wait_for_timeout(1500)
    page.wait_for_url("**/contact")
    page.go_back()
    page.wait_for_timeout(1500)
    page.wait_for_url("**/locators")
    locators_page.click_add_item()
    expect(locators_page.hot_deal_alert).to_be_visible()
    locators_page.select_country("Japan")
    expect(locators_page.country_selector).to_have_value("Japan")
    locators_page.fill_search_and_tag("Playwright", "QA-automation")
    expect(locators_page.search_input).to_have_value("Playwright")
    expect(locators_page.filter_tag_input).to_have_value("QA-automation")
    expect(locators_page.user_avatar).to_be_visible()
    locators_page.click_reload()
    expect(locators_page.settings_badge).to_be_visible()
    expect(locators_page.status_message).to_have_text("All systems operational")
    expect(locators_page.username_text).to_have_text("Username: Alice")
    expect(locators_page.task_one).to_be_visible()
    expect(locators_page.headphones_stock).to_have_text("12")
    