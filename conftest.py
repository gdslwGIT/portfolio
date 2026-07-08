import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.web_inputs_page import WebInputsPage

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

