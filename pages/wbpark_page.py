from playwright.sync_api import Page

class WebparkPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.header = page.locator("h1")
        self.parking_lot_select = page.locator("#parkingLot")
        self.entry_date_input = page.locator("#entryDate")
        self.entry_time_input = page.locator("#entryTime")
        self.exit_date_input = page.locator("#exitDate")
        self.exit_time_input = page.locator("#exitTime")
        self.calculate_btn = page.locator("#calculateCost")
        self.result_box = page.locator("#result")
        self.book_now_btn = page.locator("a:has-text('Book Now!')")

        self.first_name_input = page.locator("#firstName")
        self.last_name_input = page.locator("#lastName")
        self.email_input = page.locator("#email")
        self.phone_input = page.locator("#phone")
        self.vehicle_size_select = page.locator("#vehicleSize")
        self.license_plate_input = page.locator("#lpNumber")
        self.continue_btn = page.locator("#continue")

        self.card_number_input = page.locator("#cardNumber")
        self.expiration_date_input = page.locator("#expirationDate")
        self.security_code_input = page.locator("#securityCode")
        self.complete_reservation_btn = page.locator("#completeReservation")

    def calculate_cost(self, parking_lot: str, entry_date: str, entry_time: str, exit_date: str, exit_time: str):
        self.parking_lot_select.select_option(parking_lot)
        self.entry_date_input.fill(entry_date)
        self.entry_time_input.fill(entry_time)
        self.exit_date_input.fill(exit_date)
        self.exit_time_input.fill(exit_time)
        self.calculate_btn.click()

    def fill_booking_details(self, first_name: str, last_name: str, email: str, phone: str, vehicle_size: str, license_plate: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.email_input.fill(email)
        self.phone_input.fill(phone)
        self.vehicle_size_select.select_option(vehicle_size)
        self.license_plate_input.fill(license_plate)
        self.continue_btn.click()

    def fill_payment_details(self, card_number: str = "5200828282828223", exp_date: str = "1027", cvc: str = "123"):
        self.card_number_input.fill(card_number)
        self.expiration_date_input.fill(exp_date)
        self.security_code_input.fill(cvc)
        self.complete_reservation_btn.click()
