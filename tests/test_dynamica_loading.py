from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.dynamic_loading_page import DynamicLoadingPage

def test_dynamic_loading_example1(page: Page, home: HomePage, dynamic_loading_page: DynamicLoadingPage):
    home.click_dynamic_loading()
    page.wait_for_url("**/dynamic-loading")
    dynamic_loading_page.example1_link.click()
    page.wait_for_url("**/dynamic-loading/1")

    expect(dynamic_loading_page.finish_text).not_to_be_visible()

    dynamic_loading_page.start_btn.click()

    expect(dynamic_loading_page.loading).to_be_visible()
    expect(dynamic_loading_page.loading).not_to_be_visible(timeout=7000)

    expect(dynamic_loading_page.finish_text).to_be_visible()
    expect(dynamic_loading_page.finish_text).to_have_text("Hello World!")


def test_dynamic_loading_example2(page: Page, home: HomePage, dynamic_loading_page: DynamicLoadingPage):
    home.click_dynamic_loading()
    page.wait_for_url("**/dynamic-loading")
    dynamic_loading_page.example2_link.click()
    page.wait_for_url("**/dynamic-loading/2")
    expect(dynamic_loading_page.finish_text).to_have_count(0)

    dynamic_loading_page.start_btn.click()

    expect(dynamic_loading_page.loading).to_be_visible()
    expect(dynamic_loading_page.loading).not_to_be_visible(timeout=7000)

    expect(dynamic_loading_page.finish_text).to_be_visible()
    expect(dynamic_loading_page.finish_text).to_have_text("Hello World!")
