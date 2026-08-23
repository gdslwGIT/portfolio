from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.google_tracking_events_page import GoogleTrackingEventsPage

def test_google_tracking_events(page: Page, home: HomePage, google_tracking_events_page: GoogleTrackingEventsPage):
    home.click_google_tracking_events()
    page.wait_for_url("**/google-tracking-events")
    page.wait_for_timeout(1000)
    expect(google_tracking_events_page.flash_message).to_have_text(
        "The page_view tracking event was triggered successfully!"
    )

    google_tracking_events_page.click_btn.click()
    expect(google_tracking_events_page.flash_message).to_have_text(
        "The click tracking event was triggered successfully!"
    )

    google_tracking_events_page.click_link.click()
    expect(google_tracking_events_page.flash_message).to_have_text(
        "The click tracking event was triggered successfully!"
    )

    google_tracking_events_page.email_input.fill("test_user@example.com")
    google_tracking_events_page.message_input.fill("This is a test message to trigger analytics submit event.")
    google_tracking_events_page.submit_btn.click()
    expect(google_tracking_events_page.flash_message).to_have_text(
        "The submit tracking event was triggered successfully!"
    )

    google_tracking_events_page.conversion_btn.click()
    expect(google_tracking_events_page.flash_message).to_have_text(
        "The conversion tracking event was triggered successfully!"
    )

    google_tracking_events_page.scrollable_div.evaluate("el => el.scrollTop = el.scrollHeight")
    page.wait_for_timeout(500)
    expect(google_tracking_events_page.flash_message).to_have_text(
        "The scroll tracking event was triggered successfully!"
    )
