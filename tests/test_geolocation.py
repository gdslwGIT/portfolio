from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.geolocation_page import GeolocationPage

def test_geolocation(context, page: Page, home: HomePage, geolocation_page: GeolocationPage):
    context.grant_permissions(["geolocation"])
    context.set_geolocation({"latitude": 55.7558, "longitude": 37.6173})
    home.click_geolocation()
    page.wait_for_url("**/geolocation")
    page.wait_for_timeout(1000)
    geolocation_page.where_i_am_button.click()
    page.wait_for_timeout(1000)
    expect(geolocation_page.lat_value).to_have_text("55.7558")
    expect(geolocation_page.lon_value).to_have_text("37.6173")
