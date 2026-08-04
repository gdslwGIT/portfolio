from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.dissapearing_elements_page import DissapearingElementsPage

def test_dissapearing_elements(page: Page, home: HomePage, dissapearing_elements_page: DissapearingElementsPage):
    home.click_dissapearing_elements()
    page.wait_for_url("**/disappearing-elements")
    page.wait_for_timeout(1000)

    while dissapearing_elements_page.starred_button.count() > 0:
        page.reload()
        page.wait_for_timeout(500)
    
    expect(dissapearing_elements_page.buttons).to_have_count(4)
    expect(dissapearing_elements_page.starred_button).not_to_be_visible()

    while dissapearing_elements_page.starred_button.count() == 0:
        page.reload()
        page.wait_for_timeout(500)

    expect(dissapearing_elements_page.buttons).to_have_count(5)
    expect(dissapearing_elements_page.starred_button).to_be_visible()
