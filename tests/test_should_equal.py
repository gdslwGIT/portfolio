from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.should_equal_page import ShouldEqualPage

def test_should_equal_page(page: Page, home: HomePage, should_equal_page: ShouldEqualPage):
    home.click_should_equal()
    page.wait_for_url("**/assertions/should-equal")

    expect(should_equal_page.header).to_be_visible()
    expect(should_equal_page.header).to_have_text("Should Equal page for Automation Testing Practice")

    expect(should_equal_page.description).to_be_visible()
    expect(should_equal_page.description).to_contain_text("should equal")

    expect(should_equal_page.equal_text).to_be_visible()
    expect(should_equal_page.input1_heading).to_be_visible()
    expect(should_equal_page.simple_div).to_be_visible()
    expect(should_equal_page.simple_div).to_have_text("A simple div")
