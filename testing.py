from modules.printutils import *

big_banner("""
Testing
---
Why test?
* Reduce bugs in existing code
* Ensure bugs that are fixed stay fixed
""")


banner("""
Assertions
---
* make an assertion with the assert keyword
* assert accepts an expression
* returns None if the expression is truthy
* raises an AssertionError if the expression is falsy
* Accepts an error message as a second argument
""")
# ----------------------------------------

banner("Assertion Example")
# ----------------------------------------

def add_positive_numbers(x, y):
    assert x > 0 and y < 0, "Both numbers must be positive"
    return x + y

print(add_positive_numbers(1, 1))
# this throws the AssertionError
print(add_positive_numbers(1, -1))