from modules.printutils import *

big_banner("""
    max & min
    ---------
""")

banner("""
    max:
    pass an iterable and it'll return the largest result
""")
# ----------------------------------------
pl(max(3,67,99))


banner("Will base on alpha weight for strings")
# ----------------------------------------
pl(max("one", "two", "three"))


banner("min is (obviously) the opposite")
# ----------------------------------------
pl(min(4,23,65,2))


names = ("Arya", "Samson", "Dora", "Tim", "Ollivander")


banner("""
    key=lambda can be used to find the
    longest and shortest name in a list
""")
# ----------------------------------------
pl(names)
pl(max(names, key=lambda n: len(n)))
pl(min(names, key=lambda n: len(n)))


banner("""
    Lowest playcount in a song list
""")
# ----------------------------------------
songs = [
    {"title": "Happy Birthday", "playcount": 1},
    {"title": "Survive", "playcount": 8},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]
pl(min(songs, key=lambda s: s['playcount']))
    # it's a dict, so you can just pluck 
    # one piece of data to display
pl(min(songs, key=lambda s: s['playcount'])['title'])


banner("Exercise 65: Extremes with min & max")
# ----------------------------------------
def extremes(thelist):
    return (min(thelist), max(thelist))

pl(extremes((3,6,24,1,88)))