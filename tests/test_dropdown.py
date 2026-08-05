from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.dropdown_page import DropdownPage

def test_dropdown(page: Page, home: HomePage, dropdown_page: DropdownPage):
    home.click_dropdown()
    page.wait_for_url("**/dropdown")
    page.wait_for_timeout(1000)

    dropdown_page.simple_dropdown.select_option("2")
    expect(dropdown_page.simple_dropdown).to_have_value("2")
    page.wait_for_timeout(1000)

    dropdown_page.elements_dropdown.select_option("50")
    expect(dropdown_page.elements_dropdown).to_have_value("50")
    page.wait_for_timeout(1000)

    dropdown_page.country_dropdown.select_option("AL")
    expect(dropdown_page.country_dropdown).to_have_value("AL")
    page.wait_for_timeout(1000)
