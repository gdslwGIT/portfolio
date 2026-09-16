from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.api_endpoints_page import ApiEndpointsPage

def test_health_check_endpoint(page: Page, home: HomePage, api_endpoints_page: ApiEndpointsPage):
    home.health_check_button.evaluate("el => el.removeAttribute('target')")
    home.click_health_check()
    page.wait_for_url("**/api/health-check")

    data = api_endpoints_page.get_json_data()
    assert data["success"] is True
    assert data["status"] == "UP"

def test_my_ip_endpoint(page: Page, home: HomePage, api_endpoints_page: ApiEndpointsPage):
    home.my_ip_api_button.evaluate("el => el.removeAttribute('target')")
    home.click_my_ip_api()
    page.wait_for_url("**/api/my-ip/")

    data = api_endpoints_page.get_json_data()
    assert "ip" in data
    assert "city" in data
    assert "country" in data
