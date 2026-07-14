from playwright.sync_api import Page


class MyBrowserPage:
    def __init__(self, page: Page):
        self.page = page
        self.show_information = page.locator("#browser-toggle")
        self.info_table = page.locator("#browser-info")
        self.browser_name = page.locator("#browser-name")
        self.cookies_enabled = page.locator("#browser-cookie")
        self.platform = page.locator("#browser-platform")

    def click_show_information(self):
        self.show_information.click()