from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.should_have_page import ShouldHavePage

def test_should_have_header_visible(page: Page, home: HomePage, should_have_page: ShouldHavePage):
    home.click_should_have()
    page.wait_for_url("**/assertions/should-have")

    expect(should_have_page.header).to_be_visible()
    expect(should_have_page.header).to_have_text("Should Have page for Automation Testing Practice")

def test_should_have_buttons_visible(page: Page, home: HomePage, should_have_page: ShouldHavePage):
    home.click_should_have()
    page.wait_for_url("**/assertions/should-have")

    expect(should_have_page.btn1).to_be_visible()
    expect(should_have_page.btn2).to_be_visible()

def test_should_have_div_css(page: Page, home: HomePage, should_have_page: ShouldHavePage):
    home.click_should_have()
    page.wait_for_url("**/assertions/should-have")

    expect(should_have_page.div1_text).to_be_visible()

def test_should_have_list_items(page: Page, home: HomePage, should_have_page: ShouldHavePage):
    home.click_should_have()
    page.wait_for_url("**/assertions/should-have")

    expect(should_have_page.list_items).to_have_count(3)
    expect(should_have_page.list_items.first).to_have_text("List item 1")

def test_should_have_input_fill(page: Page, home: HomePage, should_have_page: ShouldHavePage):
    home.click_should_have()
    page.wait_for_url("**/assertions/should-have")

    expect(should_have_page.input1).to_be_visible()
    should_have_page.input1.fill("test input")
    expect(should_have_page.input1).to_have_value("test input")
