from modules.printutils import *

big_banner("""
Dictionary Concepts
----------------------------------------

• Key/Value Pairs
  • Key: DESCRIBEs the data
  • Value: REPRESENTs the data
• You CAN leave in a trailing comma, 
just like javascript
""")


banner("Example dictionary")
# ----------------------------------------
instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number"
}
print(instructor)

banner("Example list of dictionaries")
# ----------------------------------------
cart = [
    {
        "name": "cat litter",
        "quantity": 3
    },
    {
        "name": "milk",
        "quantity": 1
    },
    {
        "name": "doritos",
        "quantity": 2
    },
]
print(cart)

