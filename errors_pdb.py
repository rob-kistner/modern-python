from modules.printutils import *

big_banner("""
    Errors: Using the Python Debugger
    (PDB)
    ---------------------------------

""")


"""
    Common PDB Commands:
    ---------------------------------
    l (list)
    n (next line)
    p (print)
    c (continue - finishes debugging)
    q (quit - but in a bad ugly way, better to just use c)

    BEWARE OF 1-LETTER VARIABLE GOTCHA!
    -----------------------------------
    Don't name variables with one letter when using PDB,
    if you do, the commands above could conflict with the 
    variables and the commands will win.
"""


# normally import at the top
import pdb

# you can also import and trace in one line…
# import pdb; pdb.set_trace()

banner("Simple example: Using PDB")
# ---------------------------------------

first = "First"
second = "Second"
    # this is the magic activate line
    # put it before the line where the code is breaking
pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)
