from playwright.sync_api import Page


class WebInputsPage:
    def __init__(self, page: Page):
        self.page = page
        self.input_number = page.locator("#input-number")
        self.input_text = page.locator("#input-text")
        self.input_password = page.locator("#input-password")
        self.input_date = page.locator("#input-date")
        self.display_inputs_button = page.locator("#btn-display-inputs")
        self.check_input_number = page.locator("#output-number")
        self.check_input_text = page.locator("#output-text")
        self.check_input_password = page.locator("#output-password")
        self.check_input_date = page.locator("#output-date")
        
    def fill_form(self, number: str , text: str , password: str, date: str):
        self.input_number.fill(number)
        self.input_text.fill(text)
        self.input_password.fill(password)
        self.input_date.fill(date)

    def click_display_inputs(self):
        self.display_inputs_button.click()
