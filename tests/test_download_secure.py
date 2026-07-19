from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.download_secure_page import DownloadSecurePage

def test_download_secure(page: Page, home: HomePage, download_secure_page: DownloadSecurePage):
    home.click_download_secure()
    page.wait_for_url("**/download-secure")
    page.wait_for_timeout(1000)
    with page.expect_download() as download_info:
        download_secure_page.click_some_file()
    
    download = download_info.value
    assert download.suggested_filename == "some-file.txt"