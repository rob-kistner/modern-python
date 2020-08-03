from modules.printutils import *

big_banner("""
    OOPS: Polymorism
    -------------------------------------
    
    An object can take on many (poly) forms (morph).

    Single class working in a similar way for 
    multiple classes.

    i.e.: len: Can work with lists, tuples, strings.
""")

banner("""1st Type: Common Method:
Base class that has a method that's
overridden by a subclass""")
# ------------------------------


class Animal:

    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method.")

class Dog( Animal ):

    def speak(self):
        return "woof"

class Cat( Animal ):

    def speak(self):
        return "meow"

margie = Cat()
albert = Dog()
nada = Animal()

print(margie.speak())
print(albert.speak())
# Error thrown here, nada is just Animal
# print(nada.speak())


banner("""2nd type: Special Methods:
The same operation works for 
different types of objects. AKA: 
magic methods.
---
Example: + is shorthand for __add__()
method. Works on numbers or strings 
and does 2 different things to each 
of those.""")
# ------------------------------

class Human:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"{self.first} {self.last}"
    
    # entry for calling len(Human)
    def __len__(self):
        return self.age

    def __add__(self, partner):
        if isinstance(partner, Human):
            return Human(first='Newborn', last=self.last, age=0)
        return "You can't add that!"

    # this is multiply
    def __mul__(self, other):
        if isinstance(other, int):
            return [self for i in range(other)]
            # this would actually make a copy instead of
            # references to the original…
            #
            # import copy from copy
            # return [copy(self) for i in range(other)]
        return "You can't multiply that!"


j = Human("Jenny", "Larsen", 47)
k = Human("Kevin", "Jones", 49)

pl(j)
pl(len(j))

l = j+k
pl(l)

m = j * 3
pl(m)


banner("""Age changed to 22 on one,
you can see that they all share the
same class members.""")
# ------------------------------
m[0].age = 22
pl(m)
[print(obj.age) for obj in m]


banner("""Having quadruplets…""")
# ----------------------------------------
quadruplets =  (k + j) * 4
pl(quadruplets)