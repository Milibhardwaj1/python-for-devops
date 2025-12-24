import requests
<<<<<<< HEAD
import os
"""
As a devops engineer, you will have to navigate through multiple
external endpoints, and you should know how to switch them with Python
"""

pj_url = "https://official-joke-api.appspot.com/random_joke"
dad_joke_url = "https://icanhazdadjoke.com/"

def get_joke(url_type,mood):
    headers = {
        "Accept": "application/json"
    }
    joke = requests.get(url=url_type,headers=headers)
    if mood == "dad":
        
        final_joke = joke.json()["joke"]
    if mood == "pj":
        final_joke = joke.json()["setup"] + joke.json()["punchline"]
    return final_joke


mood = input("Which joke would you like to hear? eg. (Dad, PJ)")
if mood == "dad":
    url_type = dad_joke_url
elif mood == "pj":
    url_type = pj_url
else:
    url_type = dad_joke_url

final_joke = get_joke(url_type,mood)

print(final_joke)
=======
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
>>>>>>> 7f5864f (Adding Day-02 practice files)
