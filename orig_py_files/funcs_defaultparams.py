from modules.printutils import *

big_banner("""
    Functions:
    Default Parameters
""")

def exponent(num, power=2):
    return num ** power

expected(
    """
    exponent(2)
    when no 2nd param is supplied, the default parameter 
    will be used, in this case: 2
    """,
    exponent(2)
)

def add(a=10, b=20):
    return a+b

expected(
    "another example with 2 defaults spec'd",
    add(5,7)
)

bl()


banner("""
    Example of specifying a function as 
    a parameter
""", spaced=False)
# ----------------------------------------
def add(a, b):
    return a+b
def subtract(a, b):
    return a-b

def math(a, b, fn=add):
    return fn(a,b)

expected(
    "math(3, 2)",
    math(3, 2)
)
expected(
    "math(3, 2, subtract)",
    math(2, 3, subtract)
)