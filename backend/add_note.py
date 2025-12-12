
import requests

# Suppose you already got token from login API response
data = {"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxNSwiZXhwIjoxNzY1NTE2MTU4fQ.0wsn--EhkobQML0z1oai4DoXw4CdPQ1zk1SGmj_d5PA"}

# Extract the token
token = data["access_token"]

# Prepare headers with Authorization
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Prepare the note data to send
payload = {
    "notes": "Hello from Python"
}

# Send POST request to add note
res = requests.post("http://127.0.0.1:8000/api/add_notes", json=payload, headers=headers)

# Print status and response
print(res.status_code)
print(res.json())
