from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.cypress_spies_page import CypressSpiesPage

def test_spies_stubs_clocks(page: Page, home: HomePage, cypress_spies_page: CypressSpiesPage):

    home.click_cypress_spies()
    page.wait_for_url("**/spies-stubs-clocks")
    page.wait_for_timeout(1000)
    page.evaluate("""
        window.gtag_calls = [];
        const originalGtag = window.gtag;
        window.gtag = (...args) => {
            window.gtag_calls.push(args);
            if (originalGtag) {
                originalGtag(...args);
            }
        };
    """)
    cypress_spies_page.click_like()
    page.wait_for_timeout(500)

    expect(cypress_spies_page.like_button).not_to_be_visible()
    expect(cypress_spies_page.feedback_message).to_have_text("Thank you for your feedback!")
    calls = page.evaluate("window.gtag_calls")
    like_call = next((call for call in calls if len(call) > 1 and call[0] == "event" and call[1] == "like"), None)
    assert like_call is not None, "Событие 'like' не было найдено среди вызовов gtag"
    assert like_call[2]["event_label"] == "Like Button"

    page.context.grant_permissions(["geolocation"])
    page.context.set_geolocation({"latitude": 48.8566, "longitude": 2.3522})
    cypress_spies_page.click_find_my_location()
    page.wait_for_timeout(1000)
    expect(cypress_spies_page.country_name).to_contain_text("France")
    expect(cypress_spies_page.lat_value).to_contain_text("Latitude: 48.8566")
    expect(cypress_spies_page.long_value).to_contain_text("Longitude: 2.3522")

    page.clock.install()
    cypress_spies_page.click_browser_method()
    page.clock.run_for(12000)
    expect(cypress_spies_page.steps).to_have_count(6)
    expect(cypress_spies_page.steps.nth(0)).to_have_text("1. Ask a Question")
    expect(cypress_spies_page.steps.nth(5)).to_have_text("6. Communicate Your Results")
