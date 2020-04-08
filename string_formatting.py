# ------------------------------
#
# String Formatting
#
# ------------------------------

import printutils as u

u.bannerline("f-xstrings")
# ----------------------------------------
x = 10
print(f"I've told you {x} times already")

print(f"Doing math in an f-string: {x+2}")


u.bannerline("standard .format method")
# ----------------------------------------
print("I've told you {} times already".format(x))

u.bannerline("ye olde method")
# ----------------------------------------
print("I've told you %s times already" % x)
