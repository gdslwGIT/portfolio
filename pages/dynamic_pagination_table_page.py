from playwright.sync_api import Page

class DynamicPaginationTablePage:
    def __init__(self, page: Page):
        self.page = page
        self.entries_select = page.locator('select[name="example_length"]')
        self.search_input = page.locator('input[type="search"]')
        self.student_name_cell = page.locator('td.sorting_1')

    def select_all_entries(self):
        self.entries_select.select_option("-1")

    def search_student(self, name: str):
        self.search_input.fill(name)
    
    def get_last_student_name(self):
        return self.student_name_cell.last.inner_text()