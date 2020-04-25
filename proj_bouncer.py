""" ------------------------------

 Bouncer code-along

   • ask for age

   • 18-21 : wristband
   • 21+ : drink, normal entry
   • too young : sorry

------------------------------ """
from printutils import *

myage = 12

age = input("How old are you? : ")

if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter, but you'll need a wristband.")
    elif age >= 21:
        print("You're good to enter and drink, enjoy!")
    else:
        print("Getta outta here kid ya bother me.")
else:
    print("Please enter an age!")
