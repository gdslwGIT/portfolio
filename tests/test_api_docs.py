from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.api_docs_page import ApiDocsPage

def test_api_docs_swagger_ui_visible(page: Page, home: HomePage, api_docs_page: ApiDocsPage):
    home.click_api_docs()
    page.wait_for_url("**/notes/api/api-docs/**")
    page.wait_for_timeout(1000)

    expect(api_docs_page.swagger_ui).to_be_visible()

def test_api_docs_info_title(page: Page, home: HomePage, api_docs_page: ApiDocsPage):
    home.click_api_docs()
    page.wait_for_url("**/notes/api/api-docs/**")
    page.wait_for_timeout(1000)

    expect(api_docs_page.info_title).to_contain_text("Notes API Documentation")

def test_api_docs_endpoints_count(page: Page, home: HomePage, api_docs_page: ApiDocsPage):
    home.click_api_docs()
    page.wait_for_url("**/notes/api/api-docs/**")
    page.wait_for_timeout(1000)

    count = api_docs_page.get_endpoints_count()
    assert count >= 10

def test_expand_endpoint(page: Page, home: HomePage, api_docs_page: ApiDocsPage):
    home.click_api_docs()
    page.wait_for_url("**/notes/api/api-docs/**")
    page.wait_for_timeout(1000)

    api_docs_page.expand_endpoint(0)
    page.wait_for_timeout(500)

    expect(api_docs_page.opblocks.first).to_be_visible()

