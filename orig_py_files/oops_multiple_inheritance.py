from modules.printutils import *

big_banner("""
    OOPS: multiple inheritance
    ----------------
    
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


banner("""
    Instantiating and showing which
    superclass gets called first during 
    init. This shows the first superclass
    in the param list getting called.
""")
# ------------------------------
jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")


banner("""Checking instances""")
# ------------------------------
print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())


banner("""Checking instances""")
# ------------------------------
print(f"captain_cook is an instance of Penguin: {isinstance(captain_cook, Penguin)}")
print(f"captain_cook is an instance of Ambulatory: {isinstance(captain_cook, Ambulatory)}")
print(f"captain_cook is an instance of Aquatic: {isinstance(captain_cook, Aquatic)}")