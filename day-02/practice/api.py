
##Mili_Example###
import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1" # server URL (API)

response = requests.get(url=api_url)

for key,value in response.json().items():
    if key == "userId":
        if value in [100,200,300]:
            print("User found")

##class example####
api_url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url=api_url)

print(response)
print(type(response))
print(response.json())
print(type(response.json()))

for key,value in response.json().items():
    if key == "completed":
        if value == False:
            print("System not working")
