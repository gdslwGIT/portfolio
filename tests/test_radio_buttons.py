from playwright.sync_api import Page,expect
from pages.home_page import HomePage
from pages.radio_buttons_page import RadioButtonsPage

def test_radio_buttons(page: Page, home: HomePage, radio_buttons_page: RadioButtonsPage):
    home.click_radio_buttons()
    page.wait_for_url("**/radio-buttons")
    page.wait_for_timeout(2000)
    expect(radio_buttons_page.blue_radio).to_be_checked()
    expect(radio_buttons_page.green_radio).to_be_disabled()
    expect(radio_buttons_page.tennis_radio).to_be_checked()
    page.wait_for_timeout(2000)
    radio_buttons_page.select_color("red")
    radio_buttons_page.select_sport("football")
    expect(radio_buttons_page.red_radio).to_be_checked()
    expect(radio_buttons_page.football_radio).to_be_checked()
    page.wait_for_timeout(2000)