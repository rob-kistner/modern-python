from modules.printutils import *
import requests
import json

big_banner("""
requests: query string
----------------------

""")


# getting the data
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={
        "term": "car",
        "limit": 5
    }
)
data = res.json()


banner("""print all jokes""")
# ------------------------------
for item in data['results']:
    pl(item['joke'])