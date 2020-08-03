from modules.printutils import *


big_banner("""
    zip
    ---
    Makes an iterator that aggregates elements 
    from each of the iterables.
""")


banner("zipping two simple lists")
# ----------------------------------------

list1 = [1,2,3]
list2 = [4,5,6]
thelists = zip(list1, list2)

bannerline("The lists")
# ----------------------------------------
print(list1)
print(list2)

bannerline("Zipped")
# ----------------------------------------
for item in thelists:
    print(item)

banner("Stops at shortest iterable")
# ----------------------------------------

list1 = [1,2,3,4,5]
list2 = [6,7,8]

bannerline("the lists")
print(list1)
print(list2)
thelists = zip(list1, list2)

bannerline("zipped")
for item in thelists:
    print(item)


banner("You're not limited to two iterables")
# ----------------------------------------

list1 = [1,2,3]
list2 = [6,7,8]
list3 = ["Hi", "Howareya", "Howdy"]

bannerline("The lists")
print(list1)
print(list2)
print(list3)

bannerline("Zipped")
thelists = zip(list1, list2, list3)
for item in thelists:
    print(item)


banner("The star operator will unpack a list that's zipped: zip(*listoflists)")
# ----------------------------------------

five_by_two = [(0,1), (1,2), (2,3), (3,4), (4,5)]
thelist = list(zip(*five_by_two))
print(five_by_two)
print(thelist)


banner("Final grades example")
# ----------------------------------------
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

"""
goal: make a dict that looks like…

final_grades = {'dan': 98, 'ang': 91, 'kate': 78}
"""

bannerline("the 3 lists")
print(midterms)
print(finals)
print(students)

bannerline("comprehension with max")
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}
print(final_grades)

bannerline("zip & map method")
final_grades = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
        )
    )
)
print(final_grades)


bannerline("zip & map averging method")
final_grades = dict(
    zip(
        students,
        map(
            lambda pair: ((pair[0] + pair[1])/2),
            zip(midterms, finals)
        )
    )
)
print(final_grades)


banner("Exercise 69")
# ----------------------------------------
def interleave(str1, str2):
    """
    return a string of interleaved 2 strings
    """
    return ''.join(''.join(x) for x in zip(str1, str2))


print(interleave("hi", "mq"))


banner("Exercise 70")
# ----------------------------------------
'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''

def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))

print(triple_and_filter([1,2,3,4]))
print(triple_and_filter([6,8,10,12]))


banner("Exercise 70")
# ----------------------------------------
def extract_full_name(lst):
    return list(map(lambda val: f"{val['first']} {val['last']}", lst))

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names))