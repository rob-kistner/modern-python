from modules.printutils import *

banner("Exercise 39")
    
    # Define a function called generate_evens
    # It should return a list of even numbers between 
    # 1 and 50(not including 50)
def generate_evens():
    return [num for num in range(1, 50)][1::2]

print(generate_evens())

    # could also do this, which is probably more clear
def generate_evens_2():
    return [num for num in range(1, 50) if num%2 == 0]


# ----------------------------------------


banner("Exercise 40")

def yell(phrase):
    return phrase.upper() + "!"
print(yell('Hi There'))
