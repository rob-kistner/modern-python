from modules.printutils import *

big_banner("""
    Functions: unpacking
    -----------------------------
    use * as argument to unpack arguments
""")


def sum_all_values(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    print(total)

nums = [1,2,3,4,5,6]
# turn the above list into a bunch of arguments
# will work on lists or tuples equally as well
sum_all_values(*nums)


banner("Unpacking dicts with **")
# ----------------------------------------

def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "Colt", "second": "Rusty"}

# display_names(names) # nope..
display_names(**names)  # yup!


def add_and_multiply_numbers(a,b,c,**kwargs):
    print(a + b * c)
    print("OTHER STUFF....")
    print(kwargs)

data = dict(a=1,b=2,c=3,d=55,name="Tony")

add_and_multiply_numbers(**data) # 7
