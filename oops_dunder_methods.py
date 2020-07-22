from modules.printutils import *

class SpecialList:
    def __init__(self, data):
        self.__data = data
    
    # custom dunder method will return the length
    # of the __data member when  len() is called 
    # via an instance of this class
    def __len__(self):
        return len(self.__data)
        # return 50 <-- this would just return 50

l1 = SpecialList([1,40,30,100])
l2 = SpecialList([])

print(len(l1))
print(len(l2))


banner("""
    The __name__ variable
""")
# ------------------------------

def say_hi():
    print(f"HI! My __name__ is {__name__}")

def say_sup():
    print(f"SUP! My __name__ is {__name__}")

say_hi()
say_sup()

""" ----------------------------------------

    If you were to import another file and run the 
    above using __name__ in an imported function instead,
    it'll return the name of the import (module, it's filename
    to be specific) instead of __main__.

---------------------------------------- """

