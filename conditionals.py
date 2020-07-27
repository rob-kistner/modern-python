""" ------------------------------
    Conditionals
------------------------------ """

from printutils import bannerline, print_ind

bannerline("Basic if/elif/else format")

print("""
if <some condition> is True:
    do something
elif <some other condition> is True:
    do something else
elif <some other condition> is True:
    do yet another something else
else:
    do a final something
""")

bannerline("Basic example")
# ----------------------------------------
name = "Jon Snow"

if name == "Arya Stark":
    print("A girl needs to be an assassin")
elif name == "Jon Snow":
    print("Go be a wildling")
else:
    print("Carry on")


bannerline("Testing comparitors")
# ----------------------------------------
if (3==3):
    print("(3==3)")

if 3==3 and 5==5:
    print("3==3 and 5==5")

if (3==3) and (5==5):
    print("(3==3) and (5==5)")

if (3 is 3) and (5 is 5):
    print("(3 is 3) and (5 is 5)")

if 1:
    print("single true value always throws true")


bannerline("Comparison operators")
# ----------------------------------------

if (3==3):
    print("== : equals")

if (1!=3):
    print("!= : not equal to")

if (3>1):
    print("> : greater than")

if (1<3):
    print("< : less than")

if (4>=3):
    print(">= : greater than or equal to")

if (2<=3):
    print("<= : less than or equal to")


bannerline("Logical AND and OR")
# ----------------------------------------
if 1 and 1:
    print("1 and 1")

if (8==1) or (8==8):
    print("(8==1) or (8==8)")

if -1 is not 1:
    print("-1 is not 1")

bannerline("== vs is")
# ----------------------------------------
a = [1,2,3]
b = [1,2,3]

print()

print("a == b : == checks the values themselves :")
print_ind(a == b)
print()
print("a is b : 'is' checks if the variables take up the same place in memory :")
print_ind(a is b)