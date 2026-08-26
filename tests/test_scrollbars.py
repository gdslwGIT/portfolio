from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.scrollbars_page import ScrollbarsPage

def test_scrollbars(page: Page, home: HomePage, scrollbars_page: ScrollbarsPage):
    home.click_scrollbars()
    page.wait_for_url("**/scrollbars")
    page.wait_for_timeout(1000)

    expect(scrollbars_page.hiding_button).to_be_attached()

    scrollbars_page.hiding_button.scroll_into_view_if_needed()
    page.wait_for_timeout(500)

    expect(scrollbars_page.hiding_button).to_be_visible()

    scrollbars_page.hiding_button.click()
    page.wait_for_timeout(500)
