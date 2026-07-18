from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.file_uploader_page import FileUploaderPage
import re

def test_file_uploader(page: Page, home: HomePage, file_uploader_page: FileUploaderPage):
    home.click_file_uploader()
    page.wait_for_url("**/upload")
    page.wait_for_timeout(1000)
    file_uploader_page.upload_file("sample.txt")
    page.wait_for_timeout(1000)
    expect(file_uploader_page.file_input).to_have_value(re.compile(r"sample\.txt"))
    file_uploader_page.click_upload_button()
    page.wait_for_timeout(1000)
    expect(file_uploader_page.upload_files_header).to_have_text("File Uploaded!")
    expect(file_uploader_page.upload_file_name).to_contain_text("sample.txt")