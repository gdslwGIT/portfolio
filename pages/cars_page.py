from playwright.sync_api import Page

class CarsPage:
    def __init__(self, page: Page):
        self.page = page
        self.car_list = page.locator("#car-list")
        self.car_cards = page.locator("#car-list .card")
        self.car_names = page.locator('[data-testid="car-name"]')
        self.car_prices = page.locator('[data-testid="car-price"]')
        self.car_images = page.locator("img.card-img-top")

    def get_car_count(self) -> int:
        return self.car_cards.count()

    def get_car_name(self, index: int = 0) -> str:
        return self.car_names.nth(index).inner_text()

    def get_car_price(self, index: int = 0) -> str:
        return self.car_prices.nth(index).inner_text()
