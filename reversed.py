from modules.printutils import *

big_banner("""
    reversed
    ---------
    returns a reversed iterator
""")

banner("""
    reversed normally returns a list_reverseiterator
    object so you'd have to convert it or loop through 
    it
""")
# ----------------------------------------

output = reversed("hello")

print(output)
pl(list(output))

output = reversed([1,2,3,4])

for item in output:
    print(item)

banner("""
    reversed could be useful if you're working
    with something that's already an iterator 
    instead of the usual <string>.reverse() or 
    [::-1] slice methods.
""")
w