from modules.printutils import *

big_banner("""
    Why Modules?
    ----------------------------------------
    • Keep python files small
    • Reuse code just by importing
    • Modules are just other python code, no big mystery
""")

banner("BUILT-IN MODULES")
# ----------------------------------------
print("https://docs.python.org/3/py-modindex.html")


banner("random")
# ----------------------------------------
    # import the whole package
# import random
    # import a couple packages, when you do this,
    # you dont have to reference the class anymore
    # choice() randint()
from random import choice, randint
    # good practice, just import one method
from random import randint as rint
    # can alias, i.e.:
    # import random as rnd
# import random as rnd

fruits = ["apple", "banana", "blueberry", "cherry", "kumkwat", "grape", "orange", "lime", "dragonfruit"]
print(choice(fruits))
print(randint(1,100))
print(rint(1,50))



banner("Exercise 74")
def contains_keyword(*args):
    import keyword
    for item in args:
        if keyword.iskeyword(item): return True
    return False

print(contains_keyword("adef", "alan"))