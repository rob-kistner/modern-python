from modules.printutils import *
import requests

big_banner("""
json requests
----------------

""")


url = "https://icanhazdadjoke.com"

banner("""
    Returning text
    
    headers={'Accept': 'text/plain'}
    will just give you the joke
""")
# ------------------------------
res = requests.get(url, headers={"Accept": "text/plain"})
data = res.text
print(data)


banner("""
    Returning json

    headers={'Accept': 'application/json'}
    gives you a json request to parse.

    Then you call res.json()
""")
# ------------------------------
res = requests.get(url, headers={"Accept": "application/json"})
data = res.json()

pl(type(data))
pl(data)
pl(data["joke"])


