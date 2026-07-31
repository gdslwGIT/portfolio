from playwright.sync_api import Page

class JQueryPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_link = page.locator('a[href="/jqueryui/menu"]')
        self.enabled_menu = page.locator('ul#menu > li > a:has-text("Enabled")')
        self.downloads_menu = page.locator('ul#menu li a:has-text("Downloads")')
        self.pdf_menu = page.locator('ul#menu li a:has-text("PDF")')

        