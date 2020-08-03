""" ----------------------------------------
    Weird Math Operations

    Exponentiation (**)
    Modulo (%)
    Integer Division (//)
---------------------------------------- """

from printutils import bannerline

""" ----------------------------------------
    Exponentiation

    To the power of
---------------------------------------- """
bannerline('Exponentiation')

# 65536: because that's 4 to the 8th power
print(4 ** 8)


""" ----------------------------------------
    Modulo

    Divides first number by second number
    and returns the remainder.
    Works with integer or float.
---------------------------------------- """
bannerline('Modulo')

# 1: because 7 divided by 3 is 2 with remainder of 1
print(7 % 3)


"""
    Example of practical use,
    figuring out if numbers are odd or even
"""
# True: it's an even number, now do something
print(8 % 4 == 0)


""" ----------------------------------------
    Integer Division
---------------------------------------- """
bannerline('Integer Division')

print(10/3) # always returns a float
print(10//3) # returns an int
