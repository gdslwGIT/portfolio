from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.cars_page import CarsPage

def test_cars_list_visible(page: Page, home: HomePage, cars_page: CarsPage):
    home.click_cars()
    page.wait_for_url("**/cars")
    page.wait_for_timeout(500)

    expect(cars_page.car_list).to_be_visible()
    expect(cars_page.car_cards).to_have_count(6)

def test_first_car_details(page: Page, home: HomePage, cars_page: CarsPage):
    home.click_cars()
    page.wait_for_url("**/cars")
    page.wait_for_timeout(500)

    expect(cars_page.car_names.first).to_have_text("VW Golf")
    expect(cars_page.car_prices.first).to_have_text("€25,000")

def test_all_cars_have_names_and_prices(page: Page, home: HomePage, cars_page: CarsPage):
    home.click_cars()
    page.wait_for_url("**/cars")
    page.wait_for_timeout(500)

    count = cars_page.get_car_count()
    assert count == 6

    for i in range(count):
        expect(cars_page.car_names.nth(i)).not_to_be_empty()
        expect(cars_page.car_prices.nth(i)).not_to_be_empty()

def test_car_images_visible(page: Page, home: HomePage, cars_page: CarsPage):
    home.click_cars()
    page.wait_for_url("**/cars")
    page.wait_for_timeout(500)

    expect(cars_page.car_images).to_have_count(6)
    for i in range(6):
        expect(cars_page.car_images.nth(i)).to_be_visible()
