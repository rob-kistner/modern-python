# ----------------------------------------
# Weird Math Operations
# -----------------------------------------
#   Exponentiation (**)
#   Modulo (%)
#   Integer Division (//)
# ----------------------------------------

import modules.print_utils as u

# Exponentiation
#
# To the power of
u.bannerline('Exponentiation')
# ----------------------------------------
print(4 ** 8) # 65536: because that's 4 to the 8th power

# Modulo
#
# Divides first number by second number
# and returns the remainder.
# Works with integer or float.
u.bannerline('Modulo')
# ----------------------------------------
print(7 % 3) # 1: because 7 divided by 3 is 2 with remainder of 1

# example of practical use, figuring out 
# if numbers are odd or even
# ----------------------------------------
print(8 % 4 == 0) # True: it's an even number, now do something

# Integer Division
#
# explanation
u.bannerline('Integer Division')
# ----------------------------------------
print(10/3) # always returns a float
print(10//3) # returns an int