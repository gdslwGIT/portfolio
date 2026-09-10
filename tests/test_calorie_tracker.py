from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.calorie_tracker_page import CalorieTrackerPage

def test_add_meal(page: Page, home: HomePage, calorie_tracker_page: CalorieTrackerPage):
    home.click_calorie_tracker()
    page.wait_for_url("**/tracalorie**")
    page.wait_for_timeout(500)

    calorie_tracker_page.add_meal("Steak Dinner", "1200")
    page.wait_for_timeout(500)

    expect(calorie_tracker_page.total_calories).to_have_text("1200")
    expect(calorie_tracker_page.items).to_have_count(1)
    expect(calorie_tracker_page.items.first).to_contain_text("Steak Dinner")

def test_add_multiple_meals(page: Page, home: HomePage, calorie_tracker_page: CalorieTrackerPage):
    home.click_calorie_tracker()
    page.wait_for_url("**/tracalorie**")
    page.wait_for_timeout(500)

    calorie_tracker_page.add_meal("Steak Dinner", "1200")
    page.wait_for_timeout(500)
    calorie_tracker_page.add_meal("Apple", "100")
    page.wait_for_timeout(500)

    expect(calorie_tracker_page.total_calories).to_have_text("1300")
    expect(calorie_tracker_page.items).to_have_count(2)

def test_edit_and_update_meal(page: Page, home: HomePage, calorie_tracker_page: CalorieTrackerPage):
    home.click_calorie_tracker()
    page.wait_for_url("**/tracalorie**")
    page.wait_for_timeout(500)

    calorie_tracker_page.add_meal("Steak Dinner", "1200")
    page.wait_for_timeout(500)

    calorie_tracker_page.click_edit_item(0)
    page.wait_for_timeout(500)
    calorie_tracker_page.update_meal("Salad", "300")
    page.wait_for_timeout(500)

    expect(calorie_tracker_page.total_calories).to_have_text("300")
    expect(calorie_tracker_page.items.first).to_contain_text("Salad")

def test_delete_meal(page: Page, home: HomePage, calorie_tracker_page: CalorieTrackerPage):
    home.click_calorie_tracker()
    page.wait_for_url("**/tracalorie**")
    page.wait_for_timeout(500)

    calorie_tracker_page.add_meal("Steak Dinner", "1200")
    page.wait_for_timeout(500)

    calorie_tracker_page.click_edit_item(0)
    page.wait_for_timeout(500)
    calorie_tracker_page.delete_meal()
    page.wait_for_timeout(500)

    expect(calorie_tracker_page.total_calories).to_have_text("0")
    expect(calorie_tracker_page.items).to_have_count(0)

def test_clear_all_meals(page: Page, home: HomePage, calorie_tracker_page: CalorieTrackerPage):
    home.click_calorie_tracker()
    page.wait_for_url("**/tracalorie**")
    page.wait_for_timeout(500)

    calorie_tracker_page.add_meal("Steak Dinner", "1200")
    page.wait_for_timeout(500)
    calorie_tracker_page.add_meal("Apple", "100")
    page.wait_for_timeout(500)

    calorie_tracker_page.clear_all()
    page.wait_for_timeout(500)

    expect(calorie_tracker_page.total_calories).to_have_text("0")
    expect(calorie_tracker_page.items).to_have_count(0)
