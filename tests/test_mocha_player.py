from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.mocha_player_page import MochaPlayerPage

def test_mocha_player_page_visible(page: Page, home: HomePage, mocha_player_page: MochaPlayerPage):
    home.click_mocha_player()
    page.wait_for_url("**/mocha-chai-sinon-player")

    expect(mocha_player_page.header).to_be_visible()
    expect(mocha_player_page.header).to_contain_text("JavaScript, Mocha, Chai, and Sinon Player")

def test_mocha_player_all_variants(page: Page, home: HomePage, mocha_player_page: MochaPlayerPage):
    page.on("dialog", lambda dialog: dialog.accept())
    home.click_mocha_player()
    page.wait_for_url("**/mocha-chai-sinon-player")

    variants = ["Mocha", "Chai", "Sinon", "Axios", "Fetch"]
    for variant in variants:
        mocha_player_page.click_template(variant)
        mocha_player_page.click_run()
        page.wait_for_timeout(1000)
        expect(mocha_player_page.report).to_be_visible()
