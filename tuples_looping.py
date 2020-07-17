from modules.printutils import *

big_banner("""
TUPLES: Looping
""")

months = ('January','February','March','April','May','June','July','August','September','October','November','December')
nums = (1, 2, 3, 3, 3)

banner("Use exact same syntax as a list")
# ----------------------------------------
for month in months:
    print(month)


banner("""
    count()
    Show number of occurances in a tuple
""")
# ----------------------------------------
print(nums)
print(f"nums.count(3): {nums.count(3)}")


banner("""
    index()
    Same as a list
""")
# ----------------------------------------
print(nums)
print(f"nums.index(3): {nums.index(3)}")


banner("Can have nested tuples")
# ----------------------------------------
nested_nums = (1, 2, 3, (4, 5), 6, 7)
print(nested_nums)
print(nested_nums[3])
print(nested_nums[3][0])