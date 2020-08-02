from modules.printutils import *

big_banner("""
    Errors: Try/Except/Else/Finally Blocks
    --------------------------------------

""")


banner("Simple form of try/except")
# ---------------------------------------
# while True:
#     try:
#         num = int(input("Please enter a number: "))
#     # problem
#     except ValueError:
#         print("That's not a number.")
#     # no problem
#     else:
#         print("Good job, you entered a number")
#         break
#     # problem and no problem
#     finally:
#        print("Runs no matter what.")

# print("Remaining logic here")


def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        return "Cannot divide by 0"
    except TypeError as err:
        return f"{err}: Params must be int or float"
    # can combine errors into a tuple
    # ----------------------------------------
    # except (ZeroDivisionError, TypeError) as err:
    #    return f"{err}: An error occured."
    else:
        return f"{a} divided by {b} is {result}"

print(divide(1, 2))
print(divide(1, 0))
print(divide(1, 'a'))