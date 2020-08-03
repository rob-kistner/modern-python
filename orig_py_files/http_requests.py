from modules.printutils import *
import requests

big_banner("""
requests package
----------------

Setting the request to a variable called res
for the example below.
""")


url = "https://www.google.com"

res = requests.get(url)


banner("""res.status_code""")
# ------------------------------
print(f"Your request to {url} returned: {res.status_code}")


banner("""res.content""")
# ------------------------------
print(res.content)