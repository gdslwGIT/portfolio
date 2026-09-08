from playwright.sync_api import Page

class BmiPage:
    def __init__(self, page: Page):
        self.page = page
        self.gender_select = page.locator("#gender")
        self.age_input = page.locator("#age")
        self.height_input = page.locator("#height")
        self.weight_input = page.locator("#weight")
        self.calculate_btn = page.locator("button:has-text('Calculate')")
        self.clear_btn = page.locator("button:has-text('Clear')")
        self.result_box = page.locator("#divResult")
        self.profile_text = page.locator("#profile")
        self.bmi_text = page.locator("#BMI")
        self.indicator_text = page.locator("#indicator")

    def calculate_bmi(self, gender: str, age: str, height: str, weight: str):
        self.gender_select.select_option(gender)
        self.age_input.fill(age)
        self.height_input.fill(height)
        self.weight_input.fill(weight)
        self.calculate_btn.click()

    def clear_form(self):
        self.clear_btn.click()
