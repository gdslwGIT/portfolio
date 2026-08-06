from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.redirector_page import RedirectorPage

def test_redirector_and_status_codes(page: Page, home: HomePage, redirector_page: RedirectorPage):
    home.click_redirector()
    page.wait_for_url("**/redirector")
    page.wait_for_timeout(1000)

    redirector_page.redirect_link.click()
    page.wait_for_url("**/status-codes")
    expect(redirector_page.status_codes_header).to_have_text("Status Codes")

    codes = ["200", "301", "404", "500"]
    for code in codes:
        page.locator(f"a[href='status-codes/{code}']").click()
        page.wait_for_url(f"**/status-codes/{code}")

        expect(page.locator(".page-layout p")).to_contain_text(f"This page returned a {code} status code")

        page.locator("a[href='/status-codes']").first.click()
        page.wait_for_url("**/status-codes")
        page.wait_for_timeout(500)
