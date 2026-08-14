from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.tooltips_page import TooltipsPage

def test_tooltips(page: Page, home: HomePage, tooltips_page: TooltipsPage):
    home.click_tooltips()
    page.wait_for_url("**/tooltips")
    page.wait_for_timeout(1000)

    def check_tooltip(btn, expected_text):
        btn.hover()
        expect(tooltips_page.tooltip_inner).to_have_text(expected_text)
        
        page.locator("h1").hover()
        expect(page.locator(".tooltip")).to_have_count(0)

    check_tooltip(tooltips_page.btn1, "Tooltip on top")
    check_tooltip(tooltips_page.btn2, "Tooltip on end")
    check_tooltip(tooltips_page.btn3, "Tooltip on bottom")
    check_tooltip(tooltips_page.btn4, "Tooltip on start")
    check_tooltip(tooltips_page.btn5, "Tooltip with HTML")
