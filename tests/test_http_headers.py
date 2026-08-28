from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.http_headers_page import HttpHeadersPage

def test_http_headers(page: Page, home: HomePage, http_headers_page: HttpHeadersPage):
    page.context.set_extra_http_headers({"X-Custom-Header": "PlaywrightTest"})
    home.click_http_headers()
    page.wait_for_url("**/http-headers")
    page.wait_for_timeout(1000)
    expect(http_headers_page.header).to_have_text("HTTP Headers page for Automation Testing Practice")
    expect(http_headers_page.get_header_value("host")).to_have_text("practice.expandtesting.com")
    expect(http_headers_page.get_header_value("x-custom-header")).to_have_text("PlaywrightTest")
