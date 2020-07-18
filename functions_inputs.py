from modules.printutils import *

big_banner("""
    Functions: Inputs
    --------------------
    • Parameters: variable in a method definition
    • Arguments: the data you pass in 
      when you call a function
""")


# simple example
# ----------------------------------------
def square(num):
    return num ** 2

print(square(4))
print(square(8))

bl()


# Happy Birthday example
# ----------------------------------------
def sing_happy_birthday(name):
    print("Happy Birthday to You")
    print("Happy Birthday to You")
    print(f"Happy Birthday Dear {name}")
    print("Happy Birthday to You!")
    print()

sing_happy_birthday("Colt")
sing_happy_birthday("Rashida")
sing_happy_birthday("Nicolette")

bl()


# Math examples
# ----------------------------------------
def add(a, b):
    return a+b

def multiply(a, b):
    return a*b

print(add(1,3))
print(multiply(5,3))

bl()


# Full Name
# ----------------------------------------
def full_name(firstname, lastname):
    return f"{firstname} {lastname}"

print(full_name('Rob', 'Kistner'))