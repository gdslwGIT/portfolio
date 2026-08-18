from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.shifting_content_page import ShiftingContentPage

def test_shifting_menu_element(page: Page, home: HomePage, shifting_content_page: ShiftingContentPage):
    home.click_shifting_content()
    page.wait_for_url("**/shifting-content")
    shifting_content_page.menu_element_link.click()
    page.wait_for_url("**/shifting-content/menu")
    page.wait_for_timeout(1000)

    box_initial = shifting_content_page.shift_element.bounding_box()
    assert box_initial is not None
    initial_x = box_initial["x"]

    page.goto(f"{page.url}?pixel_shift=100")
    page.wait_for_timeout(1000)

    box_shifted = shifting_content_page.shift_element.bounding_box()
    assert box_shifted is not None
    assert abs(box_shifted["x"] - initial_x) == 100
def test_shifting_image_element(page: Page, home: HomePage, shifting_content_page: ShiftingContentPage):
    home.click_shifting_content()
    page.wait_for_url("**/shifting-content")
    shifting_content_page.image_element_link.click()
    page.wait_for_url("**/shifting-content/image")
    page.wait_for_timeout(1000)

    box_initial = shifting_content_page.shift_element.bounding_box()
    assert box_initial is not None
    initial_x = box_initial["x"]
    page.goto(f"{page.url}?pixel_shift=100")
    page.wait_for_timeout(1000)

    box_shifted = shifting_content_page.shift_element.bounding_box()
    assert box_shifted is not None
    assert abs(box_shifted["x"] - initial_x) == 100


def test_shifting_list_element(page: Page, home: HomePage, shifting_content_page: ShiftingContentPage):
    home.click_shifting_content()
    page.wait_for_url("**/shifting-content")
    shifting_content_page.list_element_link.click()
    page.wait_for_url("**/shifting-content/list")
    page.wait_for_timeout(1000)

    def get_target_index():
        count = shifting_content_page.list_items.count()
        for i in range(count):
            if "Important Information You're Looking For" in shifting_content_page.list_items.nth(i).inner_text():
                return i
        return -1

    initial_index = get_target_index()
    assert initial_index != -1, "Target list item not found!"

    shifted = False
    for _ in range(5):
        page.reload()
        page.wait_for_timeout(1000)
        current_index = get_target_index()
        if current_index != initial_index and current_index != -1:
            shifted = True
            break

    assert shifted, f"Expected the list item to shift, but it stayed at index {initial_index}"
