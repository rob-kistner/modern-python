# ------------------------------
#
# Variables
#
# ------------------------------

import modules.print_utils as u

u.banner("Variables")

# Multiple assignment
#
# You can actually assign multiple variables at once
# like the below, even though that may not be clear
u.bannerline('Multiple Assignment')
# ----------------------------------------
all, at, once = 5, 10, 15

print(all)
print(at)
print(once)


# Naming Conventions
#
# Just printing out some variable naming conventions
u.bannerline('Naming Conventions')
# ----------------------------------------
print("""
Most VARIABLES should be snake_case :
-------------------------------------
    the_first_variable = "Hi there"
""")

print("""
Most VARIABLES should be lowercase :
------------------------------------
    damnedright = 3
""")

print("""
...except CONSTANTS, which should be all UPPERCASE :
----------------------------------------------------
    PI = 3.1415
""")

print("""
Class names should be UpperCamelCase :
--------------------------------------
    class UserInfo
""")

print("""
Private variables should be surrounded with dunders :
-----------------------------------------------------
    __private_info__ = 5.93817
""")


