from modules.printutils import *
import json

big_banner("""Dicts:
Comprehension
""")

numbers = dict(first=1, second=2, third=3)
instructor = {
    "name": "Colt",
    "favorite_language": "Python",
    "44": "my favorite number",
    "color": "purple"
}

squared_numbers = { key: value ** 2 for key, value in numbers.items() }
jprint(numbers)
jprint(squared_numbers)


banner("key is the number, value is the square")
# ----------------------------------------
numbers = {num: num**2 for num in [1,2,3,4,5]}
jprint(numbers)


banner("created from two strings")
# ----------------------------------------
str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
jprint(combo)


banner("Capitalize all keys & values")
# ----------------------------------------
yelling_instructor = {k.upper():v.upper() for k, v in instructor.items()}
jprint(yelling_instructor)


banner("Interpret even or odd number into a dict")
# ----------------------------------------
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# num_list = range(1, 100)
nums = { num:("even" if num%2 == 0 else "odd") for num in num_list }
jprint(nums)


banner("Only cap a key if it matches a certain key")
# ----------------------------------------
yelling_instructor = {
    (k.upper() if k is "color" else k):v.upper() 
    for k, v in instructor.items()
    }
jprint(yelling_instructor)