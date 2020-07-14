
from modules.printutils import *

banner('''
swapping items in a list

Similar to javascript destructuring.
''')
# ----------------------------------------

names = ['James', 'Michelle']

expected('names', names)

banner('names[0], names[1] = names[1], names[0]')
# ----------------------------------------
names[0], names[1] = names[1], names[0]
print(names)