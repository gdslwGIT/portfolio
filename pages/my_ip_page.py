from playwright.sync_api import Page


class MyIpPage:
    def __init__(self,page:Page):
        self.page = page
        self.ipv4 = page.locator("#ipv4")
        self.ipv6 = page.locator("#ipv6")
        self.country = page.locator("#country")
        self.city = page.locator("#city")
        self.timezone = page.locator("#timezone")