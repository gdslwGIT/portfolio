from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.add_remove_page import AddRemovePage

def test_add_remove_elements(home: HomePage, page: Page, add_remove_page: AddRemovePage):
    home.click_add_remove()
    page.wait_for_url("**/add-remove-elements")
    page.wait_for_timeout(1000)
    expect(add_remove_page.delete_button).to_have_count(0)
    add_remove_page.add_element()
    expect(add_remove_page.delete_button).to_have_count(1)
    page.wait_for_timeout(1000)
    add_remove_page.add_element()
    page.wait_for_timeout(1000)
    add_remove_page.add_element()
    expect(add_remove_page.delete_button).to_have_count(3)
    add_remove_page.delete_element()
    expect(add_remove_page.delete_button).to_have_count(2)
    add_remove_page.delete_element()
    expect(add_remove_page.delete_button).to_have_count(1)
    page.wait_for_timeout(1000)
    add_remove_page.delete_element()
    expect(add_remove_page.delete_button).to_have_count(0)