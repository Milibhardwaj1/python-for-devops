import requests

api_url = "https://dog.ceo/api/breeds/image/random"

response = requests.get(url=api_url)

for key, value in response.json().items():
    print(key, value)

