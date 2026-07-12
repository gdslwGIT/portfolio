from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.dynamic_table_page import DynamicTablePage

def test_dynamic_table(page: Page, home: HomePage, dynamic_table_page: DynamicTablePage):
    home.click_dynamic_table()
    page.wait_for_url("**/dynamic-table")
    table_cpu = dynamic_table_page.get_chrome_cpu_value()
    yellow_text = dynamic_table_page.get_yellow_label_text()
    assert table_cpu in yellow_text