from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.dynamic_pagination_table_page import DynamicPaginationTablePage

def test_dynamic_pagination_table(page: Page, home: HomePage, dynamic_pagination_table_page: DynamicPaginationTablePage):
    home.click_dynamic_pagination_table()
    page.wait_for_url("**/dynamic-pagination-table")
    page.wait_for_timeout(1500)
    dynamic_pagination_table_page.select_all_entries()
    page.wait_for_timeout(1500)
    assert dynamic_pagination_table_page.get_last_student_name() == "Sophia Anderson"
    dynamic_pagination_table_page.search_student("Jane Smith")
    page.wait_for_timeout(1500)
    assert dynamic_pagination_table_page.student_name_cell.inner_text() == "Jane Smith"