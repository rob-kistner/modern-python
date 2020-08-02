""" ------------------------------

    Variables

------------------------------ """

from printutils import banner, bannerline, expected

banner("Variables")


""" ----------------------------------------
    Multiple assignment

    You can actually assign multiple variables at once
    like the below, even though that may not be clear
---------------------------------------- """
bannerline('Multiple Assignment')

all, at, once = 5, 10, 15

print(all)
print(at)
print(once)

""" ----------------------------------------
    Naming Conventions

    Just printing out some variable naming conventions
---------------------------------------- """
bannerline('Naming Conventions')

expected(
    "Most VARIABLES should be snake_case :",
    'the_first_variable = "Hi there"'
)

expected(
    "Most VARIABLES should be lowercase :",
    "damnedright = 3"
)

expected(
    "...except CONSTANTS, which should be all UPPERCASE :",
    "PI = 3.1415"
)

expected(
    "Class names should be UpperCamelCase :",
    "class UserInfo"
)

expected(
    "Private variables should be surrounded with dunders :",
    "__private_info__ = 5.93817"
)
