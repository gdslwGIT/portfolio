from playwright.sync_api import Page

class CalorieTrackerPage:
    def __init__(self, page: Page):
        self.page = page
        self.item_name_input = page.locator("#item-name")
        self.item_calories_input = page.locator("#item-calories")
        self.add_meal_button = page.locator("button.add-btn")
        self.update_meal_button = page.locator("button.update-btn")
        self.delete_meal_button = page.locator("button.delete-btn")
        self.back_button = page.locator("button.back-btn")
        self.clear_all_button = page.locator("ul.right a.clear-btn")
        self.total_calories = page.locator("span.total-calories")
        self.item_list = page.locator("#item-list")
        self.items = page.locator("#item-list li.collection-item")

    def add_meal(self, name: str, calories: str):
        self.item_name_input.fill(name)
        self.item_calories_input.fill(calories)
        self.add_meal_button.click()

    def click_edit_item(self, item_index: int = 0):
        self.items.nth(item_index).locator("a.secondary-content").click()

    def update_meal(self, name: str, calories: str):
        self.item_name_input.fill(name)
        self.item_calories_input.fill(calories)
        self.update_meal_button.click()

    def delete_meal(self):
        self.delete_meal_button.click()

    def clear_all(self):
        self.page.evaluate("localStorage.clear(); location.reload();")
