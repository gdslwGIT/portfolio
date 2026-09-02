from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.random_number_page import RandomNumberPage

def test_random_number(page: Page, home: HomePage, random_number_page: RandomNumberPage):
    home.click_random_number()
    page.wait_for_url("**/random-number")
    page.wait_for_timeout(500)
    
    expect(random_number_page.header).to_have_text("Random Number for Automation Testing")
    expect(random_number_page.random_number_box).to_be_visible()
    
    first_val = random_number_page.get_number_value()
    assert 0 <= first_val < 1, f"Expected number in range [0, 1), got {first_val}"
    
    page.reload()
    page.wait_for_timeout(500)
    
    second_val = random_number_page.get_number_value()
    assert 0 <= second_val < 1, f"Expected number in range [0, 1), got {second_val}"
