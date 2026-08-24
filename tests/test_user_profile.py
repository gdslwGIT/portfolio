import pytest
from playwright.sync_api import Page, expect
from pages.user_profile_page import UserProfilePage

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_user_profiles(page: Page, user_profile_page: UserProfilePage, user_id):
    page.goto(f"https://practice.expandtesting.com/users/{user_id}")
    page.wait_for_timeout(1000)

    expect(user_profile_page.header).to_have_text("User Profile page for Automation Testing Practice")
    expect(user_profile_page.welcome_message).to_have_text(f"Welcome user{user_id}")
