import urllib.request
import json
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.my_ip_page import MyIpPage

def test_my_ip(home: HomePage, my_ip_page: MyIpPage, page: Page):
    with urllib.request.urlopen("https://api.ipify.org?format=json") as response:
        current_ip = json.loads(response.read().decode())["ip"]
    home.click_my_ip()
    page.wait_for_url("**/my-ip")
    page.wait_for_timeout(1000)
    expect(my_ip_page.ipv4).to_have_text(f"IPv4: {current_ip}")
    expect(my_ip_page.country).to_be_visible()
    expect(my_ip_page.city).to_be_visible()
    expect(my_ip_page.timezone).to_be_visible()