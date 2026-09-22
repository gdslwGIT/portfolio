from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.should_include_page import ShouldIncludePage

def test_should_include_page(page: Page, home: HomePage, should_include_page: ShouldIncludePage):
    home.click_should_include()
    page.wait_for_url("**/assertions/should-include")

    expect(should_include_page.header).to_be_visible()
    expect(should_include_page.header).to_contain_text("Should Include")
    expect(should_include_page.header).to_contain_text("Automation Testing Practice")

    expect(should_include_page.description).to_be_visible()
    expect(should_include_page.description).to_contain_text("should include")
    expect(should_include_page.description).to_contain_text("array or object")

    expect(should_include_page.input1_heading).to_be_visible()
    expect(should_include_page.input1_heading).to_contain_text("input1")
