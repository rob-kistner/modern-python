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

