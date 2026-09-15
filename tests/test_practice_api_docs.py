from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.practice_api_docs_page import PracticeApiDocsPage

def test_practice_api_docs_visible(page: Page, home: HomePage, practice_api_docs_page: PracticeApiDocsPage):
    home.click_practice_api_docs()
    page.wait_for_url("**/api/api-docs/**")
    page.wait_for_timeout(1000)

    expect(practice_api_docs_page.swagger_ui).to_be_visible()

def test_practice_api_docs_endpoints_count(page: Page, home: HomePage, practice_api_docs_page: PracticeApiDocsPage):
    home.click_practice_api_docs()
    page.wait_for_url("**/api/api-docs/**")
    page.wait_for_timeout(1000)

    count = practice_api_docs_page.get_endpoints_count()
    assert count >= 6

def test_execute_health_check_in_ui(page: Page, home: HomePage, practice_api_docs_page: PracticeApiDocsPage):
    home.click_practice_api_docs()
    page.wait_for_url("**/api/api-docs/**")
    page.wait_for_timeout(1000)

    practice_api_docs_page.execute_endpoint_by_id("healthCheck")
    status = practice_api_docs_page.get_live_response_status("healthCheck")
    expect(status).to_contain_text("200")

def test_execute_random_color_in_ui(page: Page, home: HomePage, practice_api_docs_page: PracticeApiDocsPage):
    home.click_practice_api_docs()
    page.wait_for_url("**/api/api-docs/**")
    page.wait_for_timeout(1000)

    practice_api_docs_page.execute_endpoint_by_id("randomColor")
    status = practice_api_docs_page.get_live_response_status("randomColor")
    expect(status).to_contain_text("200")

def test_execute_random_number_in_ui(page: Page, home: HomePage, practice_api_docs_page: PracticeApiDocsPage):
    home.click_practice_api_docs()
    page.wait_for_url("**/api/api-docs/**")
    page.wait_for_timeout(1000)

    practice_api_docs_page.execute_endpoint_by_id("randomNumber")
    status = practice_api_docs_page.get_live_response_status("randomNumber")
    expect(status).to_contain_text("200")

def test_execute_server_time_in_ui(page: Page, home: HomePage, practice_api_docs_page: PracticeApiDocsPage):
    home.click_practice_api_docs()
    page.wait_for_url("**/api/api-docs/**")
    page.wait_for_timeout(1000)

    practice_api_docs_page.execute_endpoint_by_id("getTime")
    status = practice_api_docs_page.get_live_response_status("getTime")
    expect(status).to_contain_text("200")

def test_execute_cars_in_ui(page: Page, home: HomePage, practice_api_docs_page: PracticeApiDocsPage):
    home.click_practice_api_docs()
    page.wait_for_url("**/api/api-docs/**")
    page.wait_for_timeout(1000)

    practice_api_docs_page.execute_endpoint_by_id("getCars")
    status = practice_api_docs_page.get_live_response_status("getCars")
    expect(status).to_contain_text("200")

def test_execute_add_numbers_in_ui(page: Page, home: HomePage, practice_api_docs_page: PracticeApiDocsPage):
    home.click_practice_api_docs()
    page.wait_for_url("**/api/api-docs/**")
    page.wait_for_timeout(1000)

    block = practice_api_docs_page.get_endpoint_by_id("addNumbers")
    block.scroll_into_view_if_needed()
    if "is-open" not in (block.get_attribute("class") or ""):
        block.locator(".opblock-summary").click()
    try_btn = block.locator(".try-out__btn")
    try_btn.wait_for(state="visible", timeout=5000)
    if "cancel" not in (try_btn.get_attribute("class") or ""):
        try_btn.click()
    practice_api_docs_page.fill_param("addNumbers", "a", "10")
    practice_api_docs_page.fill_param("addNumbers", "b", "20")
    execute_btn = block.locator(".btn.execute")
    execute_btn.wait_for(state="visible", timeout=5000)
    execute_btn.click()

    status = practice_api_docs_page.get_live_response_status("addNumbers")
    expect(status).to_contain_text("200")
