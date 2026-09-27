import time
from api.notes_api import NotesApiClient

def test_notes_api_health_check(notes_api: NotesApiClient):
    response = notes_api.health_check()
    assert response.status == 200

    data = response.json()
    assert data["success"] is True
    assert data["message"] == "Notes API is Running"

def test_notes_api_user_auth_and_profile(notes_api: NotesApiClient):
    unique_email = f"user_{int(time.time() * 1000)}@testqa.com"
    password = "TestPassword123!"

    reg_resp = notes_api.register_user(name="QA Tester", email=unique_email, password=password)
    assert reg_resp.status == 201
    assert reg_resp.json()["success"] is True

    login_resp = notes_api.login_user(email=unique_email, password=password)
    assert login_resp.status == 200
    token = login_resp.json()["data"]["token"]
    assert token is not None

    notes_api.set_token(token)

    profile_resp = notes_api.get_profile()
    assert profile_resp.status == 200
    profile_data = profile_resp.json()["data"]
    assert profile_data["email"] == unique_email

    update_resp = notes_api.update_profile(name="Updated Tester", phone="1234567890", company="QA Corp")
    assert update_resp.status == 200
    assert update_resp.json()["data"]["name"] == "Updated Tester"

def test_notes_api_login_invalid_credentials(notes_api: NotesApiClient):
    response = notes_api.login_user(email="non_existing_user_999@test.com", password="wrong_password")
    assert response.status in [400, 401]
    assert response.json()["success"] is False

def test_notes_api_notes_crud_lifecycle(notes_api: NotesApiClient):
    unique_email = f"notes_user_{int(time.time() * 1000)}@testqa.com"
    password = "TestPassword123!"

    notes_api.register_user(name="Notes Owner", email=unique_email, password=password)
    login_resp = notes_api.login_user(email=unique_email, password=password)
    token = login_resp.json()["data"]["token"]
    notes_api.set_token(token)

    create_resp = notes_api.create_note(title="Buy Milk", description="Need 2 cartons of milk", category="Home")
    assert create_resp.status == 200
    created_note = create_resp.json()["data"]
    note_id = created_note["id"]
    assert created_note["title"] == "Buy Milk"
    assert created_note["completed"] is False

    get_resp = notes_api.get_note_by_id(note_id)
    assert get_resp.status == 200
    assert get_resp.json()["data"]["id"] == note_id

    list_resp = notes_api.get_notes()
    assert list_resp.status == 200
    all_notes = list_resp.json()["data"]
    assert any(n["id"] == note_id for n in all_notes)

    update_resp = notes_api.update_note(
        note_id=note_id,
        title="Buy Oat Milk",
        description="Changed to oat milk",
        completed=False,
        category="Home"
    )
    assert update_resp.status == 200
    assert update_resp.json()["data"]["title"] == "Buy Oat Milk"

    patch_resp = notes_api.update_note_completed(note_id=note_id, completed=True)
    assert patch_resp.status == 200
    assert patch_resp.json()["data"]["completed"] is True

    delete_resp = notes_api.delete_note(note_id)
    assert delete_resp.status == 200

    check_deleted = notes_api.get_note_by_id(note_id)
    assert check_deleted.status in [400, 404]
