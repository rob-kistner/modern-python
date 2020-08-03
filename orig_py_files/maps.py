from modules.printutils import *

big_banner("""
    MAPS
    ----------
    format is: map(<lambda>, <iterable>)

    Run the lambda over each member of 
    the iterable
""")


nums = [2, 4, 6, 8, 10]
doubles = map(lambda x:x*2, nums)


banner("the original list prior to map")
# ----------------------------------------
print(nums)


banner("the map is iterable")
# ----------------------------------------
for num in doubles:
    print(num)


banner("Woah…maps disappear after you use them the first time")
# ----------------------------------------
print(tuple(doubles))


banner("String map example")
# ----------------------------------------
people = ["Darcy", "Christina", "Dana", "Annabel"]
peeps = map(lambda name: name.upper(), people)
print(tuple(peeps))


banner("Exercise 62")
# ----------------------------------------
def decrement_list(thelist):
    return list(map(lambda item: item-1, thelist))

print(decrement_list([1,2,3,4,5]))