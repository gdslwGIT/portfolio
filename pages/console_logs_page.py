from playwright.sync_api import Page

class ConsoleLogsPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.btn_log = page.locator("#btn-log")
        self.btn_warn = page.locator("#btn-warn")
        self.btn_error = page.locator("#btn-error")
        self.btn_info = page.locator("#btn-info")
        self.btn_debug = page.locator("#btn-debug")
        self.btn_table = page.locator("#btn-table")
