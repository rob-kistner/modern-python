from modules.printutils import *

big_banner("""
    OOPS: MRO (Multiple Resolution Order)
    -------------------------------------
    
    There are 3 ways to refer to MRO:

    1) __mro__ attribute on class
    2) mro() method on the class
    3) use the built-in help(cls) method
""")


class Aquatic:

    def __init__(self, name):
        print("AQUATIC init")
        self.name = name

    def swim(self):
       return f"{self.name} is swimming."

    def greet(self):
       return f"I am {self.name} of the sea!"

class Ambulatory:

    def __init__(self, name):
        print("AMBULATORY init")
        self.name = name

    def walk(self):
        return f"{self.name} goes for a walk."

    def greet(self):
        return f"I am {self.name} of the land!"

class Penguin(Ambulatory, Aquatic):

    def __init__(self, name):
        print("PENGUIN init")
        super().__init__(name)
        # could call the 2nd superclass manually…
        # if you did, might be better to explicitly
        # call ALL superclasses. i.e.:
        # Ambulatory.__init__(self, name)
        Aquatic.__init__(self, name)


banner("""Instantiate classes""")
# ------------------------------
jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")

banner("""Run mro on Penguin…""")
# ------------------------------
pl(Penguin.__mro__)
pl(Penguin.mro())
# best for human readibility, but opens 
# the help environment
# help(Penguin)


banner("""
A deeper defined example, 
inheritance looks like…
..A
./ \\
B   C
.\\ /
..D
""")
# ------------------------------

class A:
    def do_something(self):
        print("Method defined in: A")
class B(A):
    pass
    # def do_something(self):
    #     print("Method defined in: B")
class C(A):
    pass
    # def do_something(self):
    #     print("Method defined in: C")
class D(B, C):
    pass
    # def do_something(self):
    #     print("Method defined in: D")

thing = D()
thing.do_something()

banner("""Showing MRO's""")
# ------------------------------
print(D.__mro__)
print(D.mro())
# help(D)