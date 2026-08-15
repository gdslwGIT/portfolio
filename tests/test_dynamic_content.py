from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.dynamic_content_page import DynamicContentPage

def test_static_and_dynamic_content(page: Page, home: HomePage, dynamic_content_page: DynamicContentPage):
    home.click_dynamic_content()
    page.wait_for_url("**/dynamic-content")
    page.wait_for_timeout(1000)

    page.goto(f"{page.url}?with_content=static")
    page.wait_for_timeout(1000)

    img1 = dynamic_content_page.row1_img.get_attribute("src")
    txt1 = dynamic_content_page.row1_txt.inner_text()

    img2 = dynamic_content_page.row2_img.get_attribute("src")
    txt2 = dynamic_content_page.row2_txt.inner_text()

    img3 = dynamic_content_page.row3_img.get_attribute("src")
    txt3 = dynamic_content_page.row3_txt.inner_text()

    page.reload()
    page.wait_for_timeout(1000)

    expect(dynamic_content_page.row1_img).to_have_attribute("src", img1)
    expect(dynamic_content_page.row1_txt).to_have_text(txt1)

    expect(dynamic_content_page.row2_img).to_have_attribute("src", img2)
    expect(dynamic_content_page.row2_txt).to_have_text(txt2)

    new_img3 = dynamic_content_page.row3_img.get_attribute("src")
    new_txt3 = dynamic_content_page.row3_txt.inner_text()
    
    assert (new_img3 != img3) or (new_txt3 != txt3), \
        "Third row was expected to be dynamic, but remained static."
