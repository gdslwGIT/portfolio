from playwright.sync_api import Page


class AutoCompletePage:
    def __init__(self, page: Page):
        self.page = page
        self.country_input = page.locator("#country")
        self.autocomplete_list = page.locator(".autocomplete-items")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.result_message = page.locator("#result")

    def type_country(self, text: str):
        self.country_input.fill(text)

    def select_suggestion(self, country_name: str):
        self.autocomplete_list.get_by_text(country_name, exact=True).click()
        
    def click_submit(self):
        self.submit_button.click()