import json
from playwright.sync_api import Page

class ApiEndpointsPage:
    def __init__(self, page: Page):
        self.page = page

    def get_json_data(self) -> dict:
        text = self.page.locator("body").inner_text()
        return json.loads(text)
