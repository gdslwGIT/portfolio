import re
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.password_checker_page import PasswordCheckerPage

def test_password_length_rule(page: Page, home: HomePage, password_checker_page: PasswordCheckerPage):
    home.click_password_checker()
    page.wait_for_url("**/secure-password-checker")
    page.wait_for_timeout(500)

    password_checker_page.enter_password("12345678")
    page.wait_for_timeout(500)

    expect(password_checker_page.length_rule).to_have_class(re.compile(r"\bvalid\b"))
    expect(password_checker_page.lowercase_rule).not_to_have_class(re.compile(r"\bvalid\b"))

def test_password_lowercase_rule(page: Page, home: HomePage, password_checker_page: PasswordCheckerPage):
    home.click_password_checker()
    page.wait_for_url("**/secure-password-checker")
    page.wait_for_timeout(500)

    password_checker_page.enter_password("a")
    page.wait_for_timeout(500)

    expect(password_checker_page.lowercase_rule).to_have_class(re.compile(r"\bvalid\b"))
    expect(password_checker_page.uppercase_rule).not_to_have_class(re.compile(r"\bvalid\b"))

def test_password_uppercase_rule(page: Page, home: HomePage, password_checker_page: PasswordCheckerPage):
    home.click_password_checker()
    page.wait_for_url("**/secure-password-checker")
    page.wait_for_timeout(500)

    password_checker_page.enter_password("A")
    page.wait_for_timeout(500)

    expect(password_checker_page.uppercase_rule).to_have_class(re.compile(r"\bvalid\b"))
    expect(password_checker_page.lowercase_rule).not_to_have_class(re.compile(r"\bvalid\b"))

def test_password_special_rule(page: Page, home: HomePage, password_checker_page: PasswordCheckerPage):
    home.click_password_checker()
    page.wait_for_url("**/secure-password-checker")
    page.wait_for_timeout(500)

    password_checker_page.enter_password("!")
    page.wait_for_timeout(500)

    expect(password_checker_page.special_rule).to_have_class(re.compile(r"\bvalid\b"))
    expect(password_checker_page.length_rule).not_to_have_class(re.compile(r"\bvalid\b"))

def test_password_all_rules_valid(page: Page, home: HomePage, password_checker_page: PasswordCheckerPage):
    home.click_password_checker()
    page.wait_for_url("**/secure-password-checker")
    page.wait_for_timeout(500)

    password_checker_page.enter_password("Abcdefg1!")
    page.wait_for_timeout(500)

    expect(password_checker_page.length_rule).to_have_class(re.compile(r"\bvalid\b"))
    expect(password_checker_page.lowercase_rule).to_have_class(re.compile(r"\bvalid\b"))
    expect(password_checker_page.uppercase_rule).to_have_class(re.compile(r"\bvalid\b"))
    expect(password_checker_page.special_rule).to_have_class(re.compile(r"\bvalid\b"))
