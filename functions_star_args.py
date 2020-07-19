from modules.printutils import *

big_banner("""
    Functions: *args
    ----------------
    represents all remaining arguments
    passed into a function
""")

# ----------------------------------------

def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_nums(1,5,23))
print(sum_all_nums(1,5,23,200,58,25,9))


banner("String comparison example")
# ----------------------------------------
def correct_info(*names):
    if "Colt" in names and "Steele" in names:
        return "Howdy Colt!"
    else:
        return "Not sure who you are…"

print(correct_info("Colt", "Mandrake", "Alex", "Steele", "Milly"))
print(correct_info("Colt", "Mandrake", "Alex", "Milly"))


banner("Exercise 57")
# ----------------------------------------
def contains_purple(*colors):
    return "purple" in colors

print(contains_purple('red', 'orange', 'purple'))
print(contains_purple('red', 'orange'))