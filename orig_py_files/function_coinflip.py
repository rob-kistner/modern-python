from random import random

"""
    looked up turnary operator, below, 
    to shorten the if statement
"""
def flip_coin():
    return ("Heads" if random() > 0.5 else "Tails")

print(flip_coin())