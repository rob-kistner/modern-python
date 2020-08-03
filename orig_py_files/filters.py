from modules.printutils import *
from json import dumps

big_banner("""
    FILTERS
    ----------
    format is: filter(<lambda>, <iterable>)

    Same as map but expects a conditional to 
    remove elements from a list
""")

banner("Filtering a number list")
# ----------------------------------------
nums = [1,2,3,4,5,6,7,8,9]
evens = list(filter(lambda x: x % 2 == 0, nums))

print(nums)  
print(evens)


banner("Filtering a user list")
# ----------------------------------------
assocs = [
    {
        "name": "Rob Kistner",
        "role": "admin",
        "title": "Art Director"
    },
    {
        "name": "Jeff Hastings",
        "role": "admin",
        "title": "Creative Director"
    },
    {
        "name": "Cindy Xiong",
        "role": "user",
        "title": "Graphic Designer"
    },
    {
        "name": "Marjan Samadi",
        "role": "user",
        "title": "Graphic Designer"
    }
]
admins = list(filter(lambda user: user["role"]=="admin", assocs))
users = list(filter(lambda user: user["role"]=="user", assocs))
print(json.dumps(admins, indent=4))
print(json.dumps(users, indent=4))


banner("""
    Return a new list with a string + 
    each value in the array, but only if 
    the value is less than 5 characters.
""")
# ----------------------------------------
names = ["Lassie", "Colt", "Rusty"]
inst = list(
    map(
        lambda name: f"Your instructor is {name}",
        filter(lambda value: len(value) < 5, names)
    )
)
print(names)
print(inst)

"""
    You also could do the above with list comprehension:
--------------------------------------------------------
    [f"Your instructor is {name}" for name in names if len(name) < 5]
"""

banner("""Using assoc list above: 
showing uppercase of all admins""")
# ----------------------------------------
upperassocs = list(
    map(
        lambda user: user["name"].upper(),
        filter(lambda u: u["role"]=="admin", assocs)
    )
)
print(upperassocs)

"""
    or…
-------
    [user["name"].upper() for user in assocs if user["name"]=="admin"]
"""


banner("Exercise 63")
# ----------------------------------------
def remove_negatives(nums):
    return list(filter(lambda num: num >= 0, nums))

print(remove_negatives([-1,3,4,-99]))
print(remove_negatives([-7,0,1,2,3,-1,4,5]))
print(remove_negatives([50,60,70]))