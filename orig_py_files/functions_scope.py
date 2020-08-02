from modules.printutils import *

big_banner("Functions: Scope")

# ----------------------------------------

def say_hello():
    instructor = "Colt"
    return f"Hello {instructor}"

say_hello()

# this would throw an error: instructor is local
# to the function only
#
# print(instructor)


banner("Global variables")

total = 0

"""
This would error out, it's assuming total 
is a local variable in the function below even 
though we meant the global total.

def increment():
    total += 1
    return total

To access that global variable, you need 
to use the global keyword…
"""

def increment():
    global total 
        # now the function is aware of the global
    total += 1
    return total

print(increment())
print(increment())
print(increment())


banner("""
    Note: you can still access the global variable 
    for read purposes, you just can't write to it 
    unless you use the global keyword…
""")

name = "Rusty"

def greet():
    print(name)

greet()

"""
But again, this wouldn't work

def greet():
    name += " Steele"
    print(name)

because you'd be trying to alter
the global variable.
"""


banner("nonlocal variables…")

def outer():
    count = 0
    def inner():
            # access the variable in 
            # the parent function
        nonlocal count
        count += 1
        return count
    return inner()

print(outer())
