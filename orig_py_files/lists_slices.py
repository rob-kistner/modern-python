
from modules.printutils import *

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

banner('''
slices

Specify[start:end:step] to get portions of a list 
back in list format.
''')
# ----------------------------------------

bannerhead('START param', '=')

expected('numbers', numbers)
expected('numbers[3:]', numbers[3:])
expected('numbers[9:]', numbers[9:])
expected('numbers[12:]', numbers[12:])
expected('numbers[-3:] -> returns the exact number of items from the end', numbers[-3:])
expected('numbers[:] -> returns the original list', numbers[:])
expected('numbers[0:] -> makes a copy of the list', numbers[0:])

bl()
bannerhead('END param', '=')

expected('numbers', numbers)
expected('numbers[:2]', numbers[:2])
expected('numbers[:4]', numbers[:4])

bl()
bannerhead('START & END params', '=')

expected('numbers', numbers)
expected('numbers[1:3]', numbers[1:3])
expected('numbers[2:-3]', numbers[2:-3])

bl()
bannerhead('STEP param', '=')

expected('numbers', numbers)
expected('numbers[1::2]', numbers[1::2])
expected('numbers[::3]', numbers[::3])
expected('numbers[1::-1] -> negative steps reverse the order', numbers[1::-1])
expected('numbers[:1:-1]', numbers[:1:-1])
expected('numbers[2::-1]', numbers[2::-1])

bl()
bannerhead('TRICKS with slices', '=')

expected('numbers', numbers)
expected('reverse the list: numbers[::-1]', numbers[::-1])
numbers[1:3] = ['a', 'b', 'c']
expected("""modify portions of a list…
numbers[1:3] = ['a', 'b', 'c']""", numbers)