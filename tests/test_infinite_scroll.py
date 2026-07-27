from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.infinite_scroll_page import InfiniteScrollPage

def test_infinite_scroll(page: Page, home: HomePage, infinite_scroll_page: InfiniteScrollPage):
    home.click_infinite_scroll()
    page.wait_for_url("**/infinite-scroll")
    page.wait_for_timeout(1000)

    initial_count = infinite_scroll_page.scroll_items.count()
    for _ in range(3):
        infinite_scroll_page.scroll_down()
        page.wait_for_timeout(1000)

    expect(infinite_scroll_page.scroll_items).to_have_count(initial_count + 3)
