from modules.printutils import *

big_banner("""
    Functions: parameter ordering
    -----------------------------
    The proper way to order parameters is:
    
    1. parameters
    2. *args
    3. default parameters
    4. **kwargs
""")

# ----------------------------------------

def display_info(a, b, *args, instructor="Colt", **kwargs):
    print(type(args))
    return [a, b, args, instructor, kwargs]

print(display_info(1, 2, 3, 4, 5, last_name="Steele", job="Instructor"))

# a - 1
# b - 2
# args (3, 4, 5)
# instructor - "Colt"
# kwargs - {'last_name': "Steele", "job": "Instructor"}
