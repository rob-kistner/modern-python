from modules.printutils import *
from random import randint

banner('basic while loop asking for user input')
# ----------------------------------------
#user_response = None
# while user_response != "please":
#  user_response = input("Ah ah ah...you didn't say the magic word: ")

# ----------------------------------------
# msg = input("What's the secret password?")
# while msg != "bananas":
#   print("INCORRECT...")
#   msg = input("What's the secret password? ")
# print("CORRECT!!!")

banner('while loop in num range')
# ----------------------------------------
# same as ...
# for num in range(1, 11):
#   print(num)
num = 1
while num <= 10:
    print(num)
    num += 1
  # note: getting fancy above, combining statements
  # on one line with a semicolon, this won't always
 # work dependent on the construct

banner('while loop with break')
# ----------------------------------------
num = 1
while num <= 10:
    print(num)
    num += 1
    if num > 5:
        print("and that\'s all folks!")
        break
