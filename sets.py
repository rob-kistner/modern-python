from modules.printutils import *

big_banner("""SETS
--------------------
• are just like formal mathematical sets
• cannot have duplicate values
• are not ordered
• cannot access items by index
""")

banner("writing a set")
# ----------------------------------------
s = {1, 4, 5}
print("setting just like a dict without key/vals: {}".format(s))

s = set({1, 4, 5, 5, 5})
print("using set function plus duplicates: {}".format(s))

s = {1, 4, 5, "a", "b", True, 8.382}
print("doesn't have to all be the same type: {}".format(s))


banner("Can use all the logical list methods…")
# ----------------------------------------
print("for loop…")
for thing in s:
    print(thing)


banner("Can get unique vals in a list by casting it to a set")
# ----------------------------------------
city_list = ["Oak Park", "Lombard", "Chicago", "Naperville", "Lisle", "Lombard", "Wheaton", "Chicago"]
print("The list: {}".format(city_list))
bl()
city_list_set = set(city_list)
print("Uniques as a set: {}".format(list(city_list_set)))
bl()
print("Or just get the unique number of items using set: {}".format(len(set(city_list))))

banner("add()")
# ----------------------------------------
s = set([1,2,3])
s.add(4)
print(s)
s.add(4)
print(s)

banner("remove()")
# ----------------------------------------
s = {1, 2, 3, 4, 5, 6}
print(s)
bl()
s.remove(3)
print(s)

banner("""discard()
is essentially remove() but doesn't throw an error
if an item in not in the set""")
# ----------------------------------------
s = {1, 2, 3, 4, 5, 6, 7}
print(s)
bl()
s.discard(10)
print("after discard(10): {}".format(s))


banner("copy()")
# ----------------------------------------
s = {1, 2, 3}
s2 = s.copy()
print(s)
print(s2)
print(s is s2)


banner("clear()")
# ----------------------------------------
s = {1, 2, 3}
print(s)
s.clear()
print(s)


print("SET MATH…")

banner("Teaching classes example…")
# ----------------------------------------
math_students = {"Matt", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matt", "Charlotte", "Mesut", "Oliver", "James"}

print("Two sets of students for two classes, what is unique…")
bl()
print("union:")
print(math_students | biology_students)
bl()
print("intersection:")
print(math_students & biology_students)