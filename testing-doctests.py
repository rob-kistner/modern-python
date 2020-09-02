"""---------------------------------------

doctests
--------

Run the below using:

    python -m doctest -v testing-doctests.py

----------------------------------------"""

def add(x, y):
    """add together x and y

    >>> add(1, 2)
    3

    >>> add(5, 3)
    8
    """
    return x * y


# Typing out the error
# --------------------
# the below would pass as a test
# because we're specifying an exact error
#
def add(x, y):
    """add together x and y

    >>> add(1, 2)
    3

    >>> add("a", 3)
    Traceback (most recent call last):
        ...
    TypeError: can only concatenate str (not "int") to str
    """
    return x + y


# QUIRK:
# doctests expects single quoted strings
# --------------------------------------
# Below will fail because we've wrote out that
# we expect double quotes, which don't match
# the single quoted string doctests expects

def say_hi():
    """
    >>> say_hi()
    "hi"
    """
    return "hi"


# QUIRK:
# Watch whitespace after boolean
# ------------------------------
# An example of a boolean return test failing
# because there's a space after True in the 
# result below

def true_that():
    """
    >>> true_that()
    True 
    """
    return True

# QUIRK:
# Dict's may not pass because they're not ordered
# -----------------------------------------------
# the returning dictionary may not be in order
# because that's the nature of dicts,
# and the test would fail if it's not in the right order

def make_dict():
    """
    >>> make_dict()
    {'a': True, 'b': True}
    """
    return {}.fromkeys(['a', 'b'], True)
