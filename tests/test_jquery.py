from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.jquery_page import JQueryPage

def test_jquery_menu_download(page: Page, home: HomePage, jquery_page: JQueryPage):
    home.click_jquery()
    page.wait_for_url("**/jqueryui")
    page.wait_for_timeout(1000)

    jquery_page.menu_link.click()
    page.wait_for_url("**/jqueryui/menu")
    page.wait_for_timeout(1000)

    jquery_page.enabled_menu.hover()
    page.wait_for_timeout(500)
    jquery_page.downloads_menu.hover()
    page.wait_for_timeout(500)

    with page.expect_download() as download_info:
        jquery_page.pdf_menu.click()
        
    download = download_info.value
    
    assert download.suggested_filename == "menu.pdf", f"Expected menu.pdf, got {download.suggested_filename}"
