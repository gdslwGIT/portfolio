from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.drag_and_drop_circles_page import DragAndDropCirclesPage

def test_drag_and_drop_circles(page: Page, home: HomePage, drag_and_drop_circles_page: DragAndDropCirclesPage):
    home.click_drag_and_drop_circles()
    page.wait_for_url("**/drag-and-drop-circles")
    page.wait_for_timeout(1000)
    expect(drag_and_drop_circles_page.red_in_target).not_to_be_visible()
    expect(drag_and_drop_circles_page.green_in_target).not_to_be_visible()
    expect(drag_and_drop_circles_page.blue_in_target).not_to_be_visible()
    drag_and_drop_circles_page.drag_circle_to_target("red")
    page.wait_for_timeout(1000)
    expect(drag_and_drop_circles_page.red_in_target).to_be_visible()
    drag_and_drop_circles_page.drag_circle_to_target("green")
    page.wait_for_timeout(1000)
    expect(drag_and_drop_circles_page.green_in_target).to_be_visible()
    drag_and_drop_circles_page.drag_circle_to_target("blue")
    page.wait_for_timeout(1000)
    expect(drag_and_drop_circles_page.blue_in_target).to_be_visible()