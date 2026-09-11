from playwright.sync_api import Page

class ColorWheelPage:
    def __init__(self, page: Page):
        self.page = page
        self.play_button = page.locator("#playBtn")
        self.reset_button = page.locator("#resetBtn")
        self.color_wheel_canvas = page.locator("#colorWheel")
        self.answers_container = page.locator("#answers")
        self.result_text = page.locator("#result")

    def click_play(self):
        self.play_button.click()

    def click_reset(self):
        self.reset_button.click()

    def get_selected_color(self) -> str:
        return self.page.evaluate("colorSelected")

    def click_color_answer(self, color_name: str):
        self.answers_container.locator(f"button:has-text('{color_name}')").click()
