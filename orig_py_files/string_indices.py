#
#   String Indices
#
from modules.printutils import *


mystr = "Marguerite"


# only the indexed letter
banner('mystr[0]', spaced=False)
# ----------------------------------------
print(mystr[0])


# up to, but not including, the specified letter index
banner('mystr[:3]', spaced=False)
# ----------------------------------------
print(mystr[:3])


# the indexed letter through the rest of the string
banner('mystr[3:]', spaced=False)
# ----------------------------------------
print(mystr[3:])


# including the 1st index up to
# but not including the 2nd index
banner('mystr[1:3]', spaced=False)
# ----------------------------------------
print(mystr[1:3])
