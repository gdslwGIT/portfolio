from playwright.sync_api import Page , expect
from pages.home_page import HomePage
from pages.broken_images_page import BrokenImagesPage

def test_broken_images(page: Page, home: HomePage, broken_images_page: BrokenImagesPage):
    home.click_broken_images()
    page.wait_for_url("**/broken-images")
    page.wait_for_timeout(1000)
    assert broken_images_page.is_image_broken(0) is True, "Image 1 should be broken"
    assert broken_images_page.is_image_broken(1) is True, "Image 2 should be broken"
    assert broken_images_page.is_image_broken(2) is False, "Image 3 should NOT be broken"