from modules.printutils import *

big_banner("Set Comprehension")

banner("create like a dict without k,v")
# ----------------------------------------
newset = {x**2 for x in range(10)}
print(newset)

newset = {char.upper() for char in 'hello'}
print(newset)

banner("making a function to count unique vowels")
def count_unique_vowels(s):
    return len({char for char in s if char in 'aeiou'})
print('happenstance')
print(count_unique_vowels('happenstance'))
