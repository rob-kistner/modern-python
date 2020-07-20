from modules.printutils import *

big_banner("""
    max & min
    ---------
""")

more_numbers = [6,1,2,8]


banner("Basic usage")
# ----------------------------------------
pl(more_numbers)
pl(sorted(more_numbers))
pl(f"note: it does not mutate the original: {more_numbers}")
pl(sorted(more_numbers, reverse=True))


banner("Can accept a tuple…")
# ----------------------------------------
pl(sorted((4,6,1,30,55,23)))


associates = [
    {
        "firstname": "Rob",
        "lastname": "Kistner",
        "role": "admin",
        "title": "Art Director"
    },
    {
        "firstname": "Jeff",
        "lastname": "Hastings",
        "role": "admin",
        "title": "Creative Director",
        "color": "orange"
    },
    {
        "firstname": "Cindy",
        "lastname": "Xiong",
        "title": "Graphic Designer"
    },
    {
        "firstname": "Marjan",
        "lastname": "Samadi",
        "role": "user",
        "title": "Graphic Designer"
    }
]


banner("""
    This will sort by how many keys are present,
    not really what we're looking for
""")
# ----------------------------------------
jprint(sorted(associates, key=len))


banner("This will sort by the user's last name")
# ----------------------------------------
jprint(
    sorted(
        associates, 
        key=lambda user: user['lastname']
    )
)


