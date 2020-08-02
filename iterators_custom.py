from modules.printutils import *

big_banner("""
    Iterators: Custom
    ---------

""")


banner("""
Counter Class
""")
# ------------------------------

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        # need to return an iterator
        # return iter("hello") <-- this works
        return self

    def __next__(self):
        if self.current < self.high + 1:
            num = self.current
            self.current += 1
            return num
        raise StopIteration

for n in Counter(50, 70):
    print(n)