
from modules.printutils import *

big_banner("""
Dictionaries:
Using 'in' with dictionaries
""")


instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number"
}

expected(
    "'name' in instructor",
    'name' in instructor
)

expected("""
    Best part of 'in': doesn't thrown an error
    if the result is False…
    'phone' in instructor
    """,
    'phone' in instructor
)

expected("""
    The above 'in' only tests keys. To test values…
    4 in instructor.values()
    """,
    4 in instructor.values()
)
