from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.wbpark_page import WebparkPage

def test_valet_parking_under_5_hours(page: Page, home: HomePage, wbpark_page: WebparkPage):
    home.click_webpark()
    page.wait_for_url("**/webpark")
    page.wait_for_timeout(500)

    wbpark_page.calculate_cost("Valet", "2026-09-07", "10:00", "2026-09-07", "14:00")
    page.wait_for_timeout(500)

    expect(wbpark_page.result_box).to_be_visible()
    expect(wbpark_page.result_box).to_contain_text("12.00€")

def test_short_term_parking(page: Page, home: HomePage, wbpark_page: WebparkPage):
    home.click_webpark()
    page.wait_for_url("**/webpark")
    page.wait_for_timeout(500)

    wbpark_page.calculate_cost("ShortTerm", "2026-09-07", "10:00", "2026-09-07", "12:00")
    page.wait_for_timeout(500)

    expect(wbpark_page.result_box).to_be_visible()
    expect(wbpark_page.result_box).to_contain_text("4.00€")

def test_economy_parking_weekly(page: Page, home: HomePage, wbpark_page: WebparkPage):
    home.click_webpark()
    page.wait_for_url("**/webpark")
    page.wait_for_timeout(500)

    wbpark_page.calculate_cost("Economy", "2026-09-07", "10:00", "2026-09-14", "10:00")
    page.wait_for_timeout(500)

    expect(wbpark_page.result_box).to_be_visible()
    expect(wbpark_page.result_box).to_contain_text("54.00€")

def test_parking_invalid_date_format(page: Page, home: HomePage, wbpark_page: WebparkPage):
    home.click_webpark()
    page.wait_for_url("**/webpark")
    page.wait_for_timeout(500)

    wbpark_page.calculate_cost("Valet", "07/09/2026", "10:00", "07/09/2026", "14:00")
    page.wait_for_timeout(500)

    expect(wbpark_page.result_box).to_be_visible()
    expect(wbpark_page.result_box).to_contain_text("Invalid entry date format!")

def test_parking_booking_flow(page: Page, home: HomePage, wbpark_page: WebparkPage):
    home.click_webpark()
    page.wait_for_url("**/webpark")
    page.wait_for_timeout(500)

    wbpark_page.calculate_cost("Valet", "2026-09-07", "10:00", "2026-09-08", "10:00")
    page.wait_for_timeout(500)
    expect(wbpark_page.result_box).to_be_visible()

    wbpark_page.book_now_btn.click()
    page.wait_for_url("**/webpark/booking/**")
    page.wait_for_timeout(500)

    wbpark_page.fill_booking_details(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        phone="1234567890",
        vehicle_size="Small car",
        license_plate="ABC1234"
    )
    page.wait_for_timeout(500)

    wbpark_page.fill_payment_details(
        card_number="5200828282828223",
        exp_date="1027",
        cvc="123"
    )
    page.wait_for_timeout(1000)
