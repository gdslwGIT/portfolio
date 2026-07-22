import pytest
import urllib.request
import json
import time
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.web_inputs_page import WebInputsPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.otp_page import OtpPage
from pages.dynamic_table_page import DynamicTablePage
from pages.dynamic_pagination_table_page import DynamicPaginationTablePage
from pages.locators_page import LocatorsPage
from pages.my_browser_page import MyBrowserPage
from pages.radio_buttons_page import RadioButtonsPage
from pages.drag_and_drop_page import DragAndDropPage
from pages.drag_and_drop_circles_page import DragAndDropCirclesPage
from pages.form_validation_page import FormValidationPage
from pages.file_uploader_page import FileUploaderPage
from pages.add_remove_page import AddRemovePage
from pages.download_secure_page import DownloadSecurePage
from pages.notification_message_page import NotificationMessagePage
from pages.autocomplete_page import AutoCompletePage
from pages.cypress_spies_page import CypressSpiesPage

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

@pytest.fixture
def forgot_password_page(page: Page) -> ForgotPasswordPage:
    return ForgotPasswordPage(page)
    
@pytest.fixture
def otp_page(page: Page) -> OtpPage:
    return OtpPage(page)

@pytest.fixture
def dynamic_table_page(page: Page) -> DynamicTablePage:
    return DynamicTablePage(page)

@pytest.fixture
def dynamic_pagination_table_page(page: Page) -> DynamicPaginationTablePage:
    return DynamicPaginationTablePage(page)

@pytest.fixture
def locators_page(page: Page) -> LocatorsPage:
    return LocatorsPage(page)

@pytest.fixture
def my_browser_page(page: Page) -> MyBrowserPage:
    return MyBrowserPage(page)

@pytest.fixture
def radio_buttons_page(page: Page) -> RadioButtonsPage:
    return RadioButtonsPage(page)

@pytest.fixture
def drag_and_drop_page(page: Page) -> DragAndDropPage:
    return DragAndDropPage(page)

@pytest.fixture
def drag_and_drop_circles_page(page: Page) -> DragAndDropCirclesPage:
    return DragAndDropCirclesPage(page)

@pytest.fixture
def form_validation_page(page: Page) -> FormValidationPage:
    return FormValidationPage(page)


@pytest.fixture
def file_uploader_page(page: Page) -> FileUploaderPage:
    return FileUploaderPage(page)

@pytest.fixture
def add_remove_page(page: Page) -> AddRemovePage:
    return AddRemovePage(page)

@pytest.fixture
def download_secure_page(page: Page) -> DownloadSecurePage:
    return DownloadSecurePage(page)

@pytest.fixture
def notification_message_page(page: Page) -> NotificationMessagePage:
    return NotificationMessagePage(page)

@pytest.fixture
def autocomplete_page(page: Page) -> AutoCompletePage:
    return AutoCompletePage(page)

@pytest.fixture
def cypress_spies_page(page: Page) -> CypressSpiesPage:
    return CypressSpiesPage(page)



@pytest.fixture
def browser_context_args(browser_context_args):
    return{**browser_context_args,"http_credentials":{"username":"admin","password":"admin"}}

@pytest.fixture
def mailbox():
    return GuerillaMail()

class GuerillaMail:
    def __init__(self):
        req = urllib.request.Request("https://api.guerrillamail.com/ajax.php?f=get_email_address", headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode())
        self.email = data["email_addr"]
        self.sid_token = data["sid_token"]

    def check_email(self):
        req = urllib.request.Request(f"https://api.guerrillamail.com/ajax.php?f=check_email&seq=0&sid_token={self.sid_token}", headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode())
        return data.get("list", [])
    
    def get_mail_body(self, email_id):
        req = urllib.request.Request(f"https://api.guerrillamail.com/ajax.php?f=fetch_email&email_id={email_id}&sid_token={self.sid_token}", headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode())
        return data.get("mail_body", "")

    def wait_for_mail(self, timeout=15):
        start_time = time.time()
        while time.time() - start_time < timeout:
            emails = self.check_email()
            if len(emails) > 1:
                return emails
            time.sleep(1)
        raise TimeoutError("No mail received within timeout")
    
    
