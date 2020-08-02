from modules.printutils import *

big_banner("""
    Errors: Raising Errors
    ----------------------

""")


banner("Simple form of raising an error")
# ---------------------------------------

# raise ValueError("This is a value error")

# raise NameError("Name error raised.")


banner("Defining errors in a function")
# ----------------------------------------

def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(text) is not str:
        raise TypeError("Text must be a string (str).")
    if type(color) is not str:
        raise TypeError("Color must be a string (str).")
    if color not in colors:
        raise ValueError(f"Color is not valid. Specify: {colors}")
    print(f"Printed {text} in {color}")

colorize("hello", "blue")
# colorize(34, "green")
# colorize("My Text", "red")