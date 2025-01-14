import requests

#I will never call Twitter the other thing

url = "https://api.twitter.com/2/tweets"

payload = {
    "text": "Test, test. Is this working?"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)

#Bluesky here