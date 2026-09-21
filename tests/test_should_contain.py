from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.should_contain_page import ShouldContainPage

def test_should_contain_page(page: Page, home: HomePage, should_contain_page: ShouldContainPage):
    home.click_should_contain()
    page.wait_for_url("**/assertions/should-contain")

    expect(should_contain_page.header).to_be_visible()
    expect(should_contain_page.header).to_contain_text("Should Contain")
    expect(should_contain_page.header).to_contain_text("Automation Testing Practice")

    expect(should_contain_page.description).to_be_visible()
    expect(should_contain_page.description).to_contain_text("should contain")
    expect(should_contain_page.description).to_contain_text("substring")

    expect(should_contain_page.input1_heading).to_be_visible()
    expect(should_contain_page.input1_heading).to_contain_text("input1")
