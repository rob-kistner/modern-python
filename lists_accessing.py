from modules.printutils import *


print("""
----------------------------------------
Qualities of a list in Python:

• Every item has an index
• List starts at 0
• There's an order to the items
""")


friends = ['Ashley', 'Matt', 'Michael']
colors = ['purple', 'teal', 'orange']


banner('The lists')
# ---------------------------
print(f'friends = {friends}')
print(f'colors = {colors}')


banner('Getting a single list value')
# --------------------------------------------------
print(f'friends[0]: {friends[0]}')
print(f'friends[1]: {friends[1]}')
# print(friends[3]) # Error: list index out of range


banner('''Getting a single list 
value with negative index''')
# ----------------------------------
print(f'friends[-1]: {friends[-1]}')
print(f'friends[-3]: {friends[-3]}')


banner('Check if value in a list')
# --------------------------------------------------
print(f'"Ashley" in friends: {"Ashley" in friends}')
