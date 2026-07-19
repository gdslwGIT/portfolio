from playwright.sync_api import Page

class DownloadSecurePage:
    def __init__(self, page: Page):
        self.page = page
        self.some_file_link = page.get_by_test_id("some-file.txt")

    def click_some_file(self):
        self.some_file_link.click()