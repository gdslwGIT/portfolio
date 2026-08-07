from playwright.sync_api import Page 

class GeolocationPage:
    def __init__(self,page: Page):
        self.page = page
        self.where_i_am_button = page.locator("#geoBtn")
        self.lat_value = page.locator("#lat-value")
        self.lon_value = page.locator("#lon-value")
        