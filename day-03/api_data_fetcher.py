import requests
import json

def search_stock(stock_name):
    api_url = "https://api.mfapi.in/mf/search"
    params = {
        "q": stock_name
    }
    headers = {
        "Accept": "application/json"
    }
    try:
        response = requests.get(url=api_url, headers=headers, params=params)
        response.raise_for_status()
        print("Status Code:", response.status_code)
        data = response.json()
    except requests.Timeout:
        raise RuntimeError("URL not reachable")


    result = [] #Empty List
    for d in data:
        if d["schemeCode"]>100000 and d["schemeCode"]<100500:
            result.append(d["schemeName"])
            print(result)
        with open("output.json", "w") as f:
            json.dump(result, f)
    print("File written successfully")

stock_name = input("Enter the name of the stock: ")
search_stock(stock_name)



