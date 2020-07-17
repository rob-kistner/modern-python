from modules.printutils import *

banner("Exercise 32")
# ----------------------------------------
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]:list2[i] for i in range(0, len(list1))}
jprint(answer)


banner("Exercise 33")
# ----------------------------------------
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {person[i][0]:person[i][1] for i in range(0, len(person))}
jprint(answer)

# actually, it's much easier…
answer = {thing[0]:thing[1] for thing in person}
jprint(answer)

# or this as well…
answer = {k:v for k,v in person}
jprint(answer)

# can also do this simple dance…
answer = dict(person)
jprint(answer)

# damn if that weren't easy :)


banner("Exercise 33")
# ----------------------------------------
answer = {L:0 for L in 'aeiou'}
jprint(answer)

# you can also use dict:fromkeys()
answer = dict.fromkeys("aeiou", 0)
jprint(answer)


banner("Exercise 34")
# ----------------------------------------
answer = {n:chr(n) for n in range(65, 91)}
jprint(answer)