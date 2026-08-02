from playwright.sync_api import Page , expect
from pages.home_page import HomePage
from pages.checkboxes_page import CheckBoxPage


def test_checkboxes(home : HomePage , checkboxes_page : CheckBoxPage, page: Page):
    home.click_checkboxes()
    page.wait_for_url("**/checkboxes")
    expect(checkboxes_page.checkbox1).not_to_be_checked()
    expect(checkboxes_page.checkbox2).to_be_checked()
    checkboxes_page.checkbox1.click()
    checkboxes_page.checkbox2.click()
    expect(checkboxes_page.checkbox1).to_be_checked()
    expect(checkboxes_page.checkbox2).not_to_be_checked()
