from modules.printutils import *

def square(num):
    return num*num

print(square(9))

# ----------------------------------------
# Lambda version
#
# • can only be one line
# • must assign to a variable
# • don't use return statement, they're automatically returned
# • usage: a throwaway function: one you might not use again
# ----------------------------------------
#

banner("A squaring lambda")
# ----------------------------------------
square2 = lambda num: num*num

print(square2(3))


banner("An add lambda")
# ----------------------------------------
add = lambda a, b: a + b

print(add(3, 10))
print(add.__name__)


banner("Lambda without a parameter")
# ----------------------------------------
say_hi = lambda: print("Hello!")


banner("Exercise 61")
# ----------------------------------------
cube = lambda num: num**3

print(cube(2))

banner("An example with tkinter")
# ----------------------------------------
"""
import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button = tk.Button(
    frame,
    text="Click Me!",
    fg="red",
    command=lambda:print("Hello!")
)
button.pack(side=tk.LEFT)
root.mainloop()
"""