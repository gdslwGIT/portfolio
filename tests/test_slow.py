from playwright.sync_api import Page , expect
from pages.home_page import HomePage
from pages.slow_page import SlowPage

def test_reveal_slow_action(page: Page , slow_page: SlowPage, home: HomePage):
    home.click_slow_page()
    page.wait_for_url("**/slow")
    expect(slow_page.result_message).to_have_text("The slow task has finished. Thanks for waiting!", timeout = 12000)
    