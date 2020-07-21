from modules.printutils import *

big_banner("""
    Errors: Try/Except Blocks
    -------------------------

""")


banner("Simple form of try/except")
# ---------------------------------------

try:
    foobar
except NameError:
    print("variable doesn't exist")
print("after the try block")

banner("Better logical error catching")
# ----------------------------------------
d = {"name": "Ricky"}

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

print(get(d, "name"))
print(get(d, "city"))
