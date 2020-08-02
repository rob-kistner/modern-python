from printutils import *

big_banner("""
    Generators
    ----------
""")


# creates generator when run
def count_up_to(max):
    count = 1
    while count <= max:
        # returns value of count then pauses here
        # until next it called
        # Note how you don't need to return 
        # anything specifically
        yield count
        count += 1

pl(count_up_to(5))

# assigns the count up generator
# to counter
counter = count_up_to(5)

# iterate through the counter generator values
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
# StopIteration error, max has been reached
# print(next(counter))


banner("""For loop through generator""")
# ------------------------------
counter = count_up_to(10)
for num in counter:
    print(num)


banner("""For loop through generator,
but call next() 1 time before starting""")
# ------------------------------
counter = count_up_to(10)
next(counter)
for num in counter:
    print(num)
