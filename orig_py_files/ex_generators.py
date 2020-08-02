from printutils import *

big_banner("""
    Exercise: Week Generator
    ------------------------
""")


# creates generator when run

def week():
    weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    for day in weekdays:
        yield day

weekgen = week()


# Above solution is said to work in the course but
# I'm getting 'function' object is not an iterator
# print(weekgen)
# print(next(week))
# print(next(week))
# print(next(week))
# print(next(week))
# print(next(week))


# this one does work though
def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"

yn = yes_or_no()
print(yn)
print(next(yn))
print(next(yn))
print(next(yn))
print(next(yn))