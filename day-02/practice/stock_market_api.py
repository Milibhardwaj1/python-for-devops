import requests
api_key = "NSZHVTK3FC17Z3UA" #STEP 1 - FETCH API KEY
api_url = "https://www.alphavantage.co/" #STEP 2 - FETCH API URL ; YE HUMARA SERVER HAI JO FIXED HOTA
symbol = input("Enter the symbol you want, Eg: AMZN, IBM: ")
interval = "5min"
query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&interval={interval}&apikey={api_key}" #STEP -3 ADD A QUERY AND PASS THE API KEY IN THAT QUERY FOR VALIDATION; JO HUMARA QUERY HAI WO CHANGE HOTA RAHGEA
print(api_url + query)
# response = requests.get()

def get_stock_market_data(symbol,is_time_series):
    response = requests.get(url=api_url+query)
    print(response.json())
    for key,value in response.json().items():
        if is_time_series:
            print(key,value)
        else :
            if key == "Time Series (Daily)":
                continue    
is_time_series = True
get_stock_market_data(symbol,is_time_series)
