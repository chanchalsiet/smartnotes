import requests

login_resp = requests.post(
    "http://127.0.0.1:8000/login",
    json={"email": "xx@gmail.com", "password": "xx"}
)

data = login_resp.json()
if "access_token" in data:
    token = data["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.post(
        "http://127.0.0.1:8000/edit_user/1",
        json={
            "full_name": "c1c",
            "first_name": "c1",
            "last_name": "c1",
            "username": "c1",
            "password": "c1",
            "status": "active"
        },
        headers=headers
    )
    print(resp.status_code, resp.text)
else:
    print("Login failed:", data)
