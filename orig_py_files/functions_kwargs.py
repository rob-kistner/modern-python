from modules.printutils import *

big_banner("Functions: Keyword Arguments")

# ----------------------------------------

def full_name(first="Colt", last="Steele"):
    return f"{first} {last}"

print(full_name(last="Kistner", first="Rob"))
print(full_name(last="Kistner"))

