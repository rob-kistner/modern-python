
from modules.printutils import *

big_banner("""
Dictionaries:
Methods
""")


instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number"
}
dict1 = dict(a=1, b=2, c=3)
dict2 = dict(a=1, b=2, c=3)
dict3 = dict(a=1, b=2, c=3)
dict4 = dict(a=1, b=2, c=3, d=4)
dict5 = dict(a=1, b=2, c=3, d=4, e=5)


banner("Variables")
# ----------------------------------------
var_dump("instructor", instructor)
bl()
var_dump("dict1 - dict5", dict1)


dict1.clear()
expected(
    "dict: clear(). Mutates original.",
    dict1
)

dict2new = dict2.copy()
expected(
    "dict: copy()",
    dict2new
)
print(f"dict2 is dict2new: {dict2 is dict2new}")


bl()
banner("fromkeys()", spaced=False)
# ----------------------------------------
    # single characters will assign key/value as expected
print({}.fromkeys("a", "b"))
    # go through list, assign each value to "unknown"
print({}.fromkeys(["email"], "unknown"))
    # better example - assign each value to "unknown"
print({}.fromkeys(["name", "title", "email"], "unknown"))
    # showing how to initialize an empty dict
print({}.fromkeys(["name", "title", "email"], None))
    # assign a single key a list value
print({}.fromkeys("a", [1, 2, 3]))
    # passing 2 strings will actually expand the first string
    # to individual keys, whoops. Need to pass a list as the
    # first argument
print({}.fromkeys("phone", "unknown"))
    # range will split up key/vals as expected
print({}.fromkeys(range(1, 6), None))


expected(
    """
    get()
    instructor.get("name")
    """,
    instructor.get("name")
)

expected(
    """
    If the key is NOT in the dict,
    it'll return None instead of an error.
    instructor.get("lastname")
    """,
    instructor.get("lastname")
)


banner("""
    pop()
    returns value of the given key,
    key IS required
""")
# ----------------------------------------
print(dict3)
print(dict3.pop('a'))
print(dict3)


banner("""
    popitem()
    returns a tuple of the last key/val
    pair of a dict
""")
# ----------------------------------------
print(dict4)
print(dict4.popitem())
print(dict4)


banner("""
    update()
""")
# ----------------------------------------
person = {"city": "Oak Park", "state": "Illinois"}
print(f"person: {person}")
bl()
instructor.update(person)
print(f"Updated instructor: {instructor}")
bl()
instructor.update({"city": "Antigua"})
print(f"Updated single key/val in instructor: {instructor}")


banner("Exercise 29: Dictionary Access")
# ----------------------------------------
# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
if food in bakery_stock:
    print(f"{bakery_stock.get(food)} left")
else:
    print("We don't make that")


banner("Exercise 30: Fromkeys")
# ----------------------------------------
#DO NOT TOUCH game_properties!
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state
initial_game_state = {}.fromkeys(game_properties, 0)
print(initial_game_state)


banner("Exercise 31: Dict Methods")
# ----------------------------------------
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = inventory.copy()
print(stock_list)

# add the value 18 to stock_list under the key "cookie"
stock_list.update({"cookie": 18})
print(stock_list)

# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop("cake")
print(stock_list)