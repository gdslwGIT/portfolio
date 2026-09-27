from playwright.sync_api import APIRequestContext, APIResponse

class NotesApiClient:
    def __init__(self, request: APIRequestContext):
        self.request = request
        self.base_url = "https://practice.expandtesting.com/notes/api"
        self.token = None

    def set_token(self, token: str):
        self.token = token

    def _headers(self):
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["x-auth-token"] = self.token
        return headers

    def health_check(self) -> APIResponse:
        return self.request.get(f"{self.base_url}/health-check")

    def register_user(self, name: str, email: str, password: str) -> APIResponse:
        return self.request.post(
            f"{self.base_url}/users/register",
            data={"name": name, "email": email, "password": password},
            headers={"Content-Type": "application/json"}
        )

    def login_user(self, email: str, password: str) -> APIResponse:
        return self.request.post(
            f"{self.base_url}/users/login",
            data={"email": email, "password": password},
            headers={"Content-Type": "application/json"}
        )

    def get_profile(self) -> APIResponse:
        return self.request.get(f"{self.base_url}/users/profile", headers=self._headers())

    def update_profile(self, name: str, phone: str = "", company: str = "") -> APIResponse:
        return self.request.patch(
            f"{self.base_url}/users/profile",
            data={"name": name, "phone": phone, "company": company},
            headers=self._headers()
        )

    def create_note(self, title: str, description: str, category: str = "Home") -> APIResponse:
        return self.request.post(
            f"{self.base_url}/notes",
            data={"title": title, "description": description, "category": category},
            headers=self._headers()
        )

    def get_notes(self) -> APIResponse:
        return self.request.get(f"{self.base_url}/notes", headers=self._headers())

    def get_note_by_id(self, note_id: str) -> APIResponse:
        return self.request.get(f"{self.base_url}/notes/{note_id}", headers=self._headers())

    def update_note(self, note_id: str, title: str, description: str, completed: bool, category: str) -> APIResponse:
        return self.request.put(
            f"{self.base_url}/notes/{note_id}",
            data={"title": title, "description": description, "completed": completed, "category": category},
            headers=self._headers()
        )

    def update_note_completed(self, note_id: str, completed: bool) -> APIResponse:
        return self.request.patch(
            f"{self.base_url}/notes/{note_id}",
            data={"completed": completed},
            headers=self._headers()
        )

    def delete_note(self, note_id: str) -> APIResponse:
        return self.request.delete(f"{self.base_url}/notes/{note_id}", headers=self._headers())
