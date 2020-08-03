from modules.printutils import *
import requests

big_banner("""
json requests
----------------

""")


url = "https://icanhazdadjoke.com"

banner("""
    headers={'Accept': 'text/plain'}
    will just give you the joke
""")
# ------------------------------
res = requests.get(url, headers={"Accept": "text/plain"})
data = res.text
print(data)


banner("""
    
""")
# ------------------------------
res = requests.get(url)
print(res)
