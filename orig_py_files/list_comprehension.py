from modules.printutils import *

big_banner("LIST COMPREHENSION")

name = "colt"
nums = [1, 2, 3, 4, 5, 6]
friends = ["ashley", "matt", "michael"]

banner("Things to remember in list comprehension")
# ----------------------------------------
print("""• Basic pattern…
    [<expression> for <iter variable> in <list>]
  
• When using an if statement, the if needs to go at the end, example…
    [num for num in numlist if num%2 == 0]
""")

banner("Variables…")
# ----------------------------------------
var_dump("name", name)
var_dump("nums", nums)
var_dump("friends", friends)


expected(
    "[x*.5 for x in nums]",
    [x*.5 for x in nums]
)

expected(
    "[char.upper() for char in name]",
    [char.upper() for char in name] 
)


expected(
    "[(friend[0].upper() + friend[1:]) for friend in friends]",
    [(friend[0].upper() + friend[1:]) for friend in friends]
)

comp = [num*10 for num in range(1,6)] 
expected(
    "[num*10 for num in range(1,6)]",
    comp
)

comp = [bool(val) for val in [1, [], '']]
expected(
    "[bool(val) for val in [1, [], '']]",
    comp
)

comp = [str(num) for num in [1,2,3,4,5]]
expected(
    "[str(num) for num in [1,2,3,4,5]]",
    comp
)

evens = [num for num in nums if num % 2 == 0]
odds = [num for num in nums if num % 2 != 0]
expected(
    """evens & odds…
    [num for num in nums if num % 2 == 0]
    [num for num in nums if num % 2 != 0]
    """,
    [evens, odds]
)

comp = [num*2 if num%2 == 0 else num/2 for num in nums]
expected(
    """A complex if/else…
    Double number if even, or half if it's odd…
    [num*2 if num%2 == 0 else num/2 for num in nums]
    """,
    comp
)

with_vowels = "This is so much fun"
comp = ''.join(char for char in with_vowels if char not in "aeiou")
expected(
    f"""Strip out vowels from a string…
    with_vowels: '{with_vowels}'
    ''.join(char for char in with_vowels if char not in 'aeiou')""",
    comp
)


banner("Exercise 20: List Comprehension")
# ----------------------------------------
answer = [char[0] for char in ["Elie", "Tim", "Matt"]]
print(answer)
answer2 = [num for num in [1,2,3,4,5,6] if num%2 == 0]
print(answer2)

banner("Exercise 21: More List Comprehension")
# ----------------------------------------
answer = [num for num in [3,4,5,6] if num in [1,2,3,4]]
print(answer)
answer2 = [name[::-1].lower() for name in ["Elie", "Tim", "Matt"]]
print(answer2)

banner("Exercise 22: Another List Comprehension Exercise")
# ----------------------------------------
answer = [num for num in range(1, 101) if num%12 == 0]
print(answer)

banner("Exercise 23: List Exercises 4")
# ----------------------------------------
answer = [char for char in "amazing" if char not in 'aeiou']
print(answer)