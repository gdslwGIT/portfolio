from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.large_deep_dom_page import LargeDeepDomPage

def test_large_deep_dom(page: Page, home: HomePage, large_deep_dom_page: LargeDeepDomPage):
    home.click_large_deep_dom()
    page.wait_for_url("**/large")
    page.wait_for_timeout(1000)

    expect(large_deep_dom_page.no_siblings_element).to_have_text("No siblings")

    expect(large_deep_dom_page.sibling_element).to_contain_text("50.1")
    cell = large_deep_dom_page.get_table_cell(50, 50)
    expect(cell).to_have_text("50.50")
    page.wait_for_timeout(1000)
