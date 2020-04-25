""" ------------------------------

    String Formatting

------------------------------ """

from printutils import bannerline as bline, bl


bline("f-xstrings")
# ----------------------------------------
x = 10
print(f"I've told you {x} times already")

print(f"Doing math in an f-string: {x+2}")


bline("standard .format method")
# ----------------------------------------
print("I've told you {} times already".format(x))


bline("ye olde method")
# ----------------------------------------
print("I've told you %s times already" % x)
