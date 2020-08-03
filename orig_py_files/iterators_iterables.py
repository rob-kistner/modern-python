from modules.printutils import *

big_banner("""
    Iterator:
    ---------
        An object that can be iterated
        on. Returns data, one element at a time
        when next() is called.
    -
    Iterable:
    ---------
        An object which returns an iterator
        when iter() is called on it.
    -
    Example:
    --------
        • 'HELLO' is an iterable, but it is not an iterator
        • iter('HELLO') returns an iterator
""")


banner("""NEXT
Iterator returns the next item. Keeps returning
when next() is called again until it reaches 
the end. Then it will raise a stop-iteration error.""")
# ------------------------------

name = "Oprah" # the iterable
it = iter(name) # the iterator
# looping starts here
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
    # out of letter in "Oprah", raises an error here…
    # ----------------------------------------
# print(next(it))

banner("""List of numbers example""")
# ------------------------------
nums = range(1, 6)
it = iter(nums)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# StopIteration error
# print(next(it))

banner("""An iterator for-loop:
Here, we're passing in a function 
to apply to each iteration.""")
# ------------------------------
def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            print("end of iterator")
            break
        else:
            # always runs this unless except
            # is reached
            print("else reached…")
            func(item)
    
my_for("Hello", print)

banner("""range(1,5)""")
# ------------------------------
my_for(range(1,5), print)

banner("""[5,6,7], print""")
# ------------------------------
my_for([5, 6, 7], print)