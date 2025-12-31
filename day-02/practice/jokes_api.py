import requests
pj_url = "https://official-joke-api.appspot.com/jokes/random/"
dad_joke_url = "https://icanhazdadjoke.com/"

headers = {

        "Accept": "application/json"

    }
response = requests.get(pj_url, headers=headers)
print(response.json())
joke = response.json()["setup"] + response.json()["punchline"]

# data = response.json()
# def get_joke():
#     if mood == "DAD":

    
#     # response = requests.get(url = dad_joke_url,headers=headers)
#     # joke = response.json()["setup"] + response.json()["punchline"]
#     # print(dir(response))
#     # return joke
# # mood = input("Enter your mood today: DAD/PJ")
# # if mood == "DAD":
# #     api_url = dad_joke_url
# # elif mood == "PJ":
# #     api_url = pj_url

# joke = get_joke()
print(joke)


