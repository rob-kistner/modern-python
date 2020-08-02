from modules.printutils import *

big_banner("""
Dictionaries:
Accessing Individual Values
""")

instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number"
}

val = instructor['name']
expected(
    """Accessing a single value of a dict:
    instructor['name']
    """,
    val
)

val = instructor[44]
expected(
    'instructor[44]',
    val
)

val = instructor['owns_dog']
expected(
    'instructor["owns_dog"]',
    val
)

property = "owns_dog"
val = instructor[property]
expected(
    """accessing by passing in a variable
    property = 'owns_dog'
    instructor[property]
    """,
    val
)

banner("Exercise: Accessing Data in a Dictionary")
# ----------------------------------------
artist = {
    "first": "Neil",
    "last": "Young",
}
full_name = artist["first"] + ' ' + artist["last"]
print(full_name)

    # note: this also works, even though the course
    # didn't allow me to do it...
full_name = f'{artist["first"]} {artist["last"]}'
print(full_name)
