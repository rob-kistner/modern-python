from modules.printutils import *

big_banner("""
    abs: absolute positive value of a number
    sum: takes iterable, and optional start 
         amount, and total it
    round: take number, and round to a specified 
           number of digits
""")

banner("abs")
# ----------------------------------------
print(abs(5))
print(abs(-5))


banner("sum")
# ----------------------------------------
print(sum([1,2,3]))
print(sum([1,2,3], 10))
print(sum([1.6,2.2,9.51]))


banner("round")
# ----------------------------------------
print(round(10.2))
print(round(104.2351, 2))