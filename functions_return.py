from modules.printutils import *

big_banner("Functions: Return keyword")

# ----------------------------------------

def print_square_of_7():
    print(7**2)

print_square_of_7()

# ----------------------------------------

def square_of_7():
    return 7**2
    # this never runs, it's after return
    print("after the return")

print(square_of_7())
