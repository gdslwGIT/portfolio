from playwright.sync_api import Page

class TablesPage:
    def __init__(self, page: Page):
        self.page = page
        self.last_name_header = page.locator("#table1 th:has-text('Last Name')")
        self.last_name_cells = page.locator("#table1 tbody tr td:first-child")
        self.first_row_edit = page.locator("#table1 tbody tr").first.locator("a.btn-primary")
        self.first_row_delete = page.locator("#table1 tbody tr").first.locator("a.btn-danger")