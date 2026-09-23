from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.should_exist_page import ShouldExistPage

def test_should_exist_page(page: Page, home: HomePage, should_exist_page: ShouldExistPage):
    home.click_should_exist()
    page.wait_for_url("**/assertions/should-exist")

    expect(should_exist_page.header).to_be_visible()
    expect(should_exist_page.header).to_contain_text("Should Exist")
    expect(should_exist_page.header).to_contain_text("Automation Testing Practice")

    expect(should_exist_page.description).to_be_visible()
    expect(should_exist_page.description).to_contain_text("should exist")
    expect(should_exist_page.description).to_contain_text("DOM")

    expect(should_exist_page.input1_heading).to_be_visible()
    expect(should_exist_page.input1_heading).to_contain_text("input1")
