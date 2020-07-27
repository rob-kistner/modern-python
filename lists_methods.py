
from modules.printutils import *

numbers = [5, 6, 7, 8, 9, 10]
first_list = [1, 2, 3, 4]
words = ['coding', 'is', 'fun']


banner('The Lists')
# ----------------------------------------
print(f'numbers: {numbers}')
print(f'first_list: {first_list}')
print(f'words: {words}')


banner('''append()
Add an item to the list''')
# ----------------------------------------
words.append('isn\'t')
words.append('it')
print(f"words.append('isn\\\'t'): {words}")


banner('''extend()
Add a list to a list''')
# ----------------------------------------
numbers.extend([5, 8, 10, 6, 5])
print(f"numbers.extend([5, 8, 10, 6, 5]): {numbers.extend([5, 8, 10, 6, 5])}")


banner('''insert(<index>, <list item>)
Add an item to a list at a certain position''')
# ----------------------------------------
numbers.insert(2, -4)
print(f"numbers.insert(2, -4): {numbers}")


banner('''index()
Shows index location of passed argument
''')
# ----------------------------------------
print(f'numbers.index(6): {numbers.index(6)}')
print(f'numbers.index(10): {numbers.index(10)}')


banner('index: with start and end...')
# ----------------------------------------
print(f'numbers.index(5): {numbers.index(5)}')
print(f'numbers.index(7, 1): {numbers.index(7, 1)}')
print(f'numbers.index(8, 2, 5): {numbers.index(8, 2, 5)}')


banner('''count()
Shows number of times result is in list''')
# ----------------------------------------
print(f'numbers.count(10): {numbers.count(10)}')


banner('''reverse()
Shows list in reverse. This is a function 
that mutates the original list.''')
# ----------------------------------------
first_list.reverse()
print(f'first_list.reverse(): {first_list}')


banner('''sort()
Sorts list, mutates the original list.''')
# ----------------------------------------
first_list.sort()
print(f'first_list.sort(): {first_list}')
first_list.append(-2)
first_list.sort()
print(f'first_list.append(-2) then sort(): {first_list}')


banner('''join()
String method, joins list members together as a string''')
# ----------------------------------------
print(f"' '.join(words): {' '.join(words)}")
print(f"''.join(words): {''.join(words)}")
print(f"'-'.join(words): {'-'.join(words)}")
print(f"', '.join(words): {', '.join(words)}")


banner('''clear()
Remove all items from a list. Mutates the original.''')
# ----------------------------------------
first_list.clear()
print(f'first_list: {first_list}')


banner('''pop()
Remove an item at specified index and return it.
Mutates the original.''')
# ----------------------------------------
first_list = [1, 2, 3, 4]
print("if there's no index specified, it'll just remove the last item")
print(f'first_list.pop(): {first_list.pop()}')
print(f'first_list: {first_list}')
print(f'first_list.pop(1): {first_list.pop(1)}')
print(f'first_list: {first_list}')


banner('''remove()
Provide a value to the remove method to have it
remove the first instance of the value in a list''')
# ----------------------------------------
first_list = [1, 2, 3, 4, 4, 4]
print(f'first_list: {first_list}')
first_list.remove(2)
print(f'first_list.remove(2): {first_list}')
first_list.remove(4)
print(f'first_list.remove(4): {first_list}')


banner('Exercise...')
# -----------------------------------------
# Create a list called instructors
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"

instructors = []
instructors.append('Colt')
instructors.append('Blue')
instructors.append('Lisa')
print('Added using append()')
print(instructors)

instructors = []
print('Added using extend()')
instructors.extend(['Colt', 'Blue', 'Lisa'])
print(instructors)