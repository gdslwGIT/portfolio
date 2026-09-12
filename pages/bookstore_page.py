from playwright.sync_api import Page

class BookstorePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator('input[placeholder="Enter keywords..."]')
        self.search_button = page.locator('button:has-text("Search")')
        self.sign_in_link = page.locator('a[href="/bookstore/user/signin"]')
        self.sign_up_link = page.locator('a[href="/bookstore/user/signup"]')
        self.cart_link = page.locator('a[href="/bookstore/cart"]')
        self.all_books_link = page.locator('a:has-text("All Books")')
        
        self.sort_dropdown = page.locator('.filter_sort-select')
        self.sort_asc_link = page.locator('a[href*="sort=asc"]')
        self.sort_desc_link = page.locator('a[href*="sort=desc"]')
        self.sort_new_link = page.locator('a[href*="sort=new_book"]')

        self.add_to_cart_buttons = page.locator('a[href*="/bookstore/add-to-cart/"]')

        self.signin_email_input = page.locator('#email')
        self.signin_password_input = page.locator('#password')
        self.signin_submit_button = page.locator('button#submit')

        self.signup_username_input = page.locator('#username')
        self.signup_email_input = page.locator('#email')
        self.signup_password_input = page.locator('#password')
        self.signup_confirm_password_input = page.locator('#password2')
        self.signup_submit_button = page.locator('button#submit')

        self.checkout_button = page.locator('a[href*="/bookstore/checkout"], a.btn:has-text("Checkout")')

        self.checkout_name_input = page.locator('input[name="name"], #name, label:has-text("Name") + input').first
        self.checkout_address_input = page.locator('input[name="address"], #address, label:has-text("Address") + input').first
        self.checkout_card_holder_input = page.locator('input[name="card_name"], input[name="cardHolderName"], #card_name, label:has-text("Card Holder Name") + input').first
        self.checkout_card_number_input = page.locator('input[name="card_number"], input[name="cardNumber"], #card_number, label:has-text("Credit Card Number") + input').first
        self.checkout_exp_month_input = page.locator('input[placeholder="MM"], input[name="exp_month"]').first
        self.checkout_exp_year_input = page.locator('input[placeholder="YYYY"], input[name="exp_year"]').first
        self.checkout_cvc_input = page.locator('input[placeholder="123"], input[name="cvc"]').first
        self.purchase_button = page.locator('button:has-text("Purchase"), input[value="Purchase"]').first

    def search_book(self, keyword: str):
        self.search_input.fill(keyword)
        self.search_button.click()

    def sort_by_asc(self):
        self.sort_dropdown.click()
        self.sort_asc_link.click()

    def sort_by_desc(self):
        self.sort_dropdown.click()
        self.sort_desc_link.click()

    def sort_by_new(self):
        self.sort_new_link.click()

    def add_first_book_to_cart(self):
        self.add_to_cart_buttons.first.click()

    def register(self, username: str, email: str, password: str):
        self.signup_username_input.fill(username)
        self.signup_email_input.fill(email)
        self.signup_password_input.fill(password)
        self.signup_confirm_password_input.fill(password)
        self.signup_submit_button.click()

    def login(self, email: str, password: str):
        self.signin_email_input.fill(email)
        self.signin_password_input.fill(password)
        self.signin_submit_button.click()

    def fill_checkout_form(self, name: str, address: str, card_holder: str, card_number: str, exp_month: str, exp_year: str, cvc: str):
        self.checkout_name_input.fill(name)
        self.checkout_address_input.fill(address)
        self.checkout_card_holder_input.fill(card_holder)
        self.checkout_card_number_input.fill(card_number)
        self.checkout_exp_month_input.fill(exp_month)
        self.checkout_exp_year_input.fill(exp_year)
        self.checkout_cvc_input.fill(cvc)
        self.purchase_button.click()

    def click_sign_in(self):
        self.sign_in_link.click()

    def click_sign_up(self):
        self.sign_up_link.click()

    def click_cart(self):
        self.cart_link.click()
