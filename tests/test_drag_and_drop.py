from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.drag_and_drop_page import DragAndDropPage


def test_drag_and_drop(page: Page, home: HomePage, drag_and_drop_page: DragAndDropPage):
    home.click_drag_and_drop()
    page.wait_for_url("**/drag-and-drop")
    page.wait_for_timeout(1000)
    expect(drag_and_drop_page.column_a).to_have_text("A")
    expect(drag_and_drop_page.column_b).to_have_text("B")
    drag_and_drop_page.drag_a_to_b()
    page.wait_for_timeout(1000)
    expect(drag_and_drop_page.column_a).to_have_text("B")
    expect(drag_and_drop_page.column_b).to_have_text("A")
    