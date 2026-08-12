from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.windows_page import WindowsPage
import re

def test_new_window(context, page: Page, home: HomePage, windows_page: WindowsPage):
    home.click_windows()
    page.wait_for_url("**/windows")
    page.wait_for_timeout(1000)

    with context.expect_page() as new_page_info:
        windows_page.click_here_link.click()

    new_page = new_page_info.value
    new_page.wait_for_load_state()

    expect(new_page).to_have_url(re.compile(r".*/windows/new"))
    expect(new_page.locator("h1")).to_have_text("Example of a new window page for Automation Testing Practice")
    new_page.close()
