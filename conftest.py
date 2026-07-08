import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.web_inputs_page import WebInputsPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage

@pytest.fixture(autouse=True)
def open_site(page: Page):
    page.route("**/*google*", lambda route: route.abort())
    page.goto("https://practice.expandtesting.com/")

    yield page

@pytest.fixture
def home(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def web_inputs(page: Page) -> WebInputsPage:
    return WebInputsPage(page)

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def register_page(page: Page) -> RegisterPage:
    return RegisterPage(page)