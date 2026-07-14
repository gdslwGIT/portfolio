from playwright.sync_api import Page , expect
from pages.home_page import HomePage
from pages.my_browser_page import MyBrowserPage

def test_my_browser_info(page: Page, home: HomePage , my_browser_page: MyBrowserPage):
    home.click_my_browser()
    page.wait_for_url("**/my-browser")
    expect(my_browser_page.show_information).to_have_text("Show Browser Information")
    expect(my_browser_page.browser_name).not_to_be_visible()
    my_browser_page.click_show_information()
    expect(my_browser_page.show_information).to_have_text("Hide Browser Information")
    expect(my_browser_page.browser_name).to_be_visible()
    expect(my_browser_page.browser_name).to_have_text("Google Chrome") 
    expect(my_browser_page.cookies_enabled).to_have_text("true")      
    my_browser_page.click_show_information()
    expect(my_browser_page.show_information).to_have_text("Show Browser Information")
    expect(my_browser_page.browser_name).not_to_be_visible()
