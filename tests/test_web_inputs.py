from playwright.sync_api import Page
from pages.home_page import HomePage

def test_navigate_to_web_inputs(home: HomePage, page: Page):
    home.click_web_inputs()
    assert page.url == "https://practice.expandtesting.com/inputs"
