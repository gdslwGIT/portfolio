from playwright.sync_api import Page


class ChallengingDomPage:
    def __init__(self, page: Page):
        self.page = page
        self.blue_button = page.locator(".large-2 a").nth(0)
        self.warning_button = page.locator(".large-2 a").nth(1)
        self.success_button = page.locator(".large-2 a").nth(2)

    def click_delete_for_row(self, row_text: str):
        row = self.page.locator("tr", has_text=row_text)
        row.locator('a[href="#delete"]').click()

    def click_edit_for_row(self, row_text: str):
        row = self.page.locator("tr", has_text=row_text)
        row.locator('a[href="#edit"]').click()