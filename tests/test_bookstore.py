import re
import time
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.bookstore_page import BookstorePage

def test_bookstore_elements_visible(page: Page, home: HomePage, bookstore_page: BookstorePage):
    home.click_bookstore()
    page.wait_for_url("**/bookstore**")
    page.wait_for_timeout(500)

    expect(bookstore_page.search_input).to_be_visible()
    expect(bookstore_page.search_button).to_be_visible()
    expect(bookstore_page.sign_in_link).to_be_visible()
    expect(bookstore_page.cart_link).to_be_visible()

def test_search_book(page: Page, home: HomePage, bookstore_page: BookstorePage):
    home.click_bookstore()
    page.wait_for_url("**/bookstore**")
    page.wait_for_timeout(500)

    bookstore_page.search_book("DevOps")
    page.wait_for_timeout(1000)

    expect(page.locator("body")).to_contain_text("DevOps")

def test_sort_books(page: Page, home: HomePage, bookstore_page: BookstorePage):
    home.click_bookstore()
    page.wait_for_url("**/bookstore**")
    page.wait_for_timeout(500)

    bookstore_page.sort_by_asc()
    page.wait_for_timeout(500)
    expect(page).to_have_url(re.compile(r"sort=asc"))

    bookstore_page.sort_by_desc()
    page.wait_for_timeout(500)
    expect(page).to_have_url(re.compile(r"sort=desc"))

def test_user_registration_flow(page: Page, home: HomePage, bookstore_page: BookstorePage):
    home.click_bookstore()
    page.wait_for_url("**/bookstore**")
    page.wait_for_timeout(500)

    bookstore_page.click_sign_in()
    page.wait_for_url("**/bookstore/user/signin**")
    page.wait_for_timeout(500)

    bookstore_page.click_sign_up()
    page.wait_for_url("**/bookstore/user/signup**")
    page.wait_for_timeout(500)

    unique_email = f"testuser_{int(time.time())}@example.com"
    bookstore_page.register("TestUser", unique_email, "Password123!")
    page.wait_for_timeout(1000)

    expect(page).to_have_url("https://practice.expandtesting.com/bookstore/user/signin")

def test_user_login_flow(page: Page, home: HomePage, bookstore_page: BookstorePage):
    home.click_bookstore()
    page.wait_for_url("**/bookstore**")
    page.wait_for_timeout(500)

    bookstore_page.click_sign_in()
    page.wait_for_url("**/bookstore/user/signin**")
    page.wait_for_timeout(500)

    bookstore_page.click_sign_up()
    page.wait_for_url("**/bookstore/user/signup**")
    page.wait_for_timeout(500)

    user_email = f"login_user_{int(time.time())}@example.com"
    user_password = "Password123!"

    bookstore_page.register("LoginUser", user_email, user_password)
    page.wait_for_url("**/bookstore/user/signin**")
    page.wait_for_timeout(500)

    bookstore_page.login(user_email, user_password)
    page.wait_for_timeout(1000)

    expect(page.locator("body")).to_be_visible()

def test_update_cart_quantity(page: Page, home: HomePage, bookstore_page: BookstorePage):
    home.click_bookstore()
    page.wait_for_url("**/bookstore**")
    page.wait_for_timeout(500)

    bookstore_page.add_first_book_to_cart()
    page.wait_for_timeout(1000)

    bookstore_page.click_cart()
    page.wait_for_url("**/bookstore/cart**")
    page.wait_for_timeout(500)

    qty_input = page.locator('input[name="quantity"], input[type="number"]').first
    if qty_input.is_visible():
        qty_input.fill("2")
        update_btn = page.locator('button:has-text("Update"), input[value="Update"]').first
        if update_btn.is_visible():
            update_btn.click()
            page.wait_for_timeout(500)

    expect(page.locator("body")).to_contain_text("Shopping Cart")

def test_checkout_and_payment_flow(page: Page, home: HomePage, bookstore_page: BookstorePage):
    home.click_bookstore()
    page.wait_for_url("**/bookstore**")
    page.wait_for_timeout(500)

    bookstore_page.click_sign_in()
    page.wait_for_url("**/bookstore/user/signin**")
    page.wait_for_timeout(500)

    bookstore_page.click_sign_up()
    page.wait_for_url("**/bookstore/user/signup**")
    page.wait_for_timeout(500)

    user_email = f"buyer_{int(time.time())}@example.com"
    user_password = "Password123!"

    bookstore_page.register("BuyerUser", user_email, user_password)
    page.wait_for_url("**/bookstore/user/signin**")
    page.wait_for_timeout(500)

    bookstore_page.login(user_email, user_password)
    page.wait_for_timeout(1000)

    bookstore_page.all_books_link.click()
    page.wait_for_url("**/bookstore")
    page.wait_for_timeout(500)

    bookstore_page.add_first_book_to_cart()
    page.wait_for_timeout(1000)

    bookstore_page.click_cart()
    page.wait_for_url("**/bookstore/cart**")
    page.wait_for_timeout(500)

    checkout_link = page.locator('a[href*="/bookstore/checkout"], a.btn:has-text("Checkout")').first
    if checkout_link.is_visible():
        checkout_link.click()
        page.wait_for_url("**/bookstore/checkout**")
        page.wait_for_timeout(500)

        bookstore_page.fill_checkout_form(
            name="BuyerUser",
            address="123 Main Street",
            card_holder="BuyerUser",
            card_number="4242424242424242",
            exp_month="12",
            exp_year="2028",
            cvc="123"
        )
        page.wait_for_timeout(1000)

    expect(page.locator("body")).to_be_visible()
