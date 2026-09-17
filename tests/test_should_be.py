from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.should_be_page import ShouldBePage

def test_should_be_header_visible(page: Page, home: HomePage, should_be_page: ShouldBePage):
    home.click_should_be()
    page.wait_for_url("**/assertions/should-be")

    expect(should_be_page.header).to_be_visible()
    expect(should_be_page.header).to_have_text("Should Be page for Automation Testing Practice")

def test_should_be_list_count(page: Page, home: HomePage, should_be_page: ShouldBePage):
    home.click_should_be()
    page.wait_for_url("**/assertions/should-be")

    expect(should_be_page.list_items).to_have_count(6)

def test_should_be_list_items_content(page: Page, home: HomePage, should_be_page: ShouldBePage):
    home.click_should_be()
    page.wait_for_url("**/assertions/should-be")

    expect(should_be_page.list_items.nth(0)).to_have_text("first")
    expect(should_be_page.list_items.nth(1)).to_have_text("second")
    expect(should_be_page.list_items.nth(2)).to_have_text("third")

def test_should_be_divs_visible(page: Page, home: HomePage, should_be_page: ShouldBePage):
    home.click_should_be()
    page.wait_for_url("**/assertions/should-be")

    expect(should_be_page.div1_heading).to_be_visible()
    expect(should_be_page.div2_heading).to_be_visible()
    expect(should_be_page.div2_text).to_be_visible()
