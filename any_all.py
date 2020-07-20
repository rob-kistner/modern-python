from printutils import *
from json import dumps

big_banner("""
    ANY & ALL
    ----------
    ALL:

    Takes iterable, returns true if 
    all elements are truthy
""")


banner("""
    Different examples using ALL
    and list comprehension
""")
# ----------------------------------------
pl(all([0,1,2,3]))

pl(all([char for char in 'eio' if char in 'aeiou']))

people = ["Charlie", "Casey", "Cody", "Carly", "Christina"]
pl(all([name[0]=="C" for name in people]))

people.append("Michael")
pl(all([name[0]=="C" for name in people]))

nums = [2, 60, 26, 18]
pl(all([num % 2 == 0 for num in nums]))


banner("""
    Different examples using ANY
    and list comprehension
""")
# ----------------------------------------
nums = [2, 60, 26, 18, 31]
pl(any([num % 2 != 0 for num in nums])) # any odd?



banner("""
    Using a generator
""")
    # FROM ANY & ALL TUTORIAL SECTION
    # ----------------------------------------

people = ["Charlie", "Alex", "Mike", "Paul", "Christina"]

listcomp = [name[0]=="C" for name in people]
pl(any(listcomp))

    # That list comp without abstraction into 
    # a list becomes a generator

pl(name[0]=="C" for name in people)
pl(any(name[0]=="C" for name in people))
pl(all(name[0]=="C" for name in people))

    # works well because you're not using it again,
    # if you were, you'd store it into a variable as
    # list comprehension

    # showing memory size differences
import sys
pl(f"generator: {sys.getsizeof(name[0]=='C' for name in people)} bytes")
pl(f"list comprehension: {sys.getsizeof([name[0]=='C' for name in people])} bytes")


banner("Exercise 64")
# ----------------------------------------
def is_all_strings( thelist ):
    return all(type(item) is str for item in thelist)

pl(is_all_strings(['1', '2', '3']))
pl(is_all_strings(['1', '2', 3]))
pl(is_all_strings(['1', '2', ('one', 'two', 'three')]))