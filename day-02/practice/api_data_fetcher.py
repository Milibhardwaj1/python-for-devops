import requests
import json
api_url = "https://api.mfapi.in/mf/search"

params = {
    "q": "hdfc"
}
headers = {
    "Accept": "application/json"
}
response = requests.get(url=api_url, headers=headers, params=params)

print("Status Code:", response.status_code)

data = response.json()
# print(type(data))
# print(data)
result = [] #Empty List
for d in data:
    if d["schemeCode"]>100000 and d["schemeCode"]<100500:
        result.append(d["schemeName"])
        print(result)
with open("output.json", "w") as f:
    json.dump(result, f)
print("File written successfully")


