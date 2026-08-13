import re
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.tables_page import TablesPage

def test_tables_sorting_and_actions(page: Page, home: HomePage, tables_page: TablesPage):
    home.click_tables()
    page.wait_for_url("**/tables")
    page.wait_for_timeout(1000)

    initial_names = tables_page.last_name_cells.all_inner_texts()
    assert len(initial_names) > 0, "Table should contain rows"

    tables_page.last_name_header.click()
    page.wait_for_timeout(500)
    sorted_asc_names = tables_page.last_name_cells.all_inner_texts()
    assert sorted_asc_names == sorted(initial_names)

    tables_page.last_name_header.click()
    page.wait_for_timeout(500)
    sorted_desc_names = tables_page.last_name_cells.all_inner_texts()
    assert sorted_desc_names == sorted(initial_names, reverse=True)

    tables_page.first_row_edit.click()
    page.wait_for_timeout(500)
    expect(page).to_have_url(re.compile(r".*#edit"))

    tables_page.first_row_delete.click()
    page.wait_for_timeout(500)
    expect(page).to_have_url(re.compile(r".*#delete"))
