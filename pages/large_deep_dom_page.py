from playwright.sync_api import Page


class LargeDeepDomPage:
    def __init__(self, page: Page):
        self.page = page
        self.no_siblings_element = page.locator("#no-siblings")
        self.sibling_element = page.locator('[id="sibling-50.1"]')
        
    def get_table_cell(self, row: int, col: int):
        return self.page.locator(f"tr.row-{row} td:nth-child({col})")
