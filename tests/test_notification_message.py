from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.notification_message_page import NotificationMessagePage

def test_notification_message(page: Page, home: HomePage, notification_message_page: NotificationMessagePage):
    home.click_notification_message()
    page.wait_for_url("**/notification-message-rendered")
    page.wait_for_timeout(1000)
    max_attempts = 10
    for _ in range(max_attempts):
        notification_message_page.click_trigger_link()
        page.wait_for_timeout(500)
        current_text = notification_message_page.flash_message.inner_text()
        if "Action successful" in current_text:
            break
    expect(notification_message_page.flash_message).to_contain_text("Action successful")