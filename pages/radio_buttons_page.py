from playwright.sync_api import Page

class RadioButtonsPage:
    def __init__(self, page: Page):
        self.page = page
        self.blue_radio = page.locator("#blue")
        self.green_radio = page.locator("#green")
        self.yellow_radio = page.locator("#yellow")
        self.black_radio = page.locator("#black")
        self.red_radio = page.locator("#red")
        self.basketball_radio = page.locator("#basketball")
        self.football_radio = page.locator("#football")
        self.tennis_radio = page.locator("#tennis")
        

    def select_color(self, color_id: str):
        self.page.locator(f"#{color_id}").click()

    def select_sport(self, sport_id: str):
        self.page.locator(f"#{sport_id}").click()