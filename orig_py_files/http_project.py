import requests
from random import randint as rnd

# get the search term
print()
topic = input("Let me tell you a joke! Give me a topic: ")

# getting the data
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url, 
    headers={
        "Accept": "application/json"
    },
    params={
        "term": topic.lower()
    }
).json()

# select a random joke
jokes_count = len(res["results"])
selected = res['results'][rnd(0, jokes_count-1)]['joke']

# print joke
if jokes_count != 0:
    print()
    print(f"I've got {jokes_count} jokes about {topic}, here's one:")
    print("------------------------------------------------")
    print()
    print(selected)
    print()
else:
    print()
    print(f"Sorry, I don't have any jokes about {topic}")