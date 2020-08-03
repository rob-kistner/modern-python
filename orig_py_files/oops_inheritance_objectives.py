from modules.printutils import *

big_banner("""
    OOPS: Inheritance & Objectives
    ----------------------
    • Inheritance, including multiple
    • Method resolution
    • Polymorphism
    • Add special methods to classes
""")

banner("""Animal and Cat base and child classes""")
# ------------------------------

# base class

class Animal:
    cool = True
    
    def make_sound(self, sound):
        print(f"This animal says {sound}")


# inheriting class
# argument passed in the base class

class Cat(Animal):
    pass

bird = Animal()
cat = Cat()

bird.make_sound('chirp')
cat.make_sound('meow')
print(cat.cool)
print(Animal.cool)

expected(
    "isinstance(cat, Animal)",
    isinstance(cat, Animal)
)
expected(
    "isinstance(cat, Cat)",
    isinstance(cat, Cat)
)
expected(
    "isinstance(cat, object)",
    isinstance(cat, object)
)
