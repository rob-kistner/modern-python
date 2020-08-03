from modules.printutils import *

big_banner("""
    OOPS: Class Attributes
    ----------------------

    Usually defined at the top of a class, 
    they are essentially static class members.
    Just like class statics, the value is shared 
    by all instances.
    
    You'll call them directly from the class name
    instead of from the instance.
""")


class User:

        # active_users class attribute, all instances
        # have access to it and can mutate it
    active_users = 0

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        User.active_users += 1

    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    def initials(self, periods=True):
        if periods:
            return f"{self.firstname[0]}.{self.lastname[0]}."
        return f"{self.firstname[0]}{self.lastname[0]}"
    
    def likes(self, thing):
        return f"{self.firstname} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday, {self.firstname}!"

    def logout(self):
        User.active_users -= 1
        return f"{self.fullname()} has been logged out."


user1 = User("Joe", "Smith", 19)
user2 = User("Blanca", "Lopez", 34)

pl(
    user1.fullname(),
    user2.fullname(),
    user2.initials(),
    user2.initials(False),
    user1.likes("rabbits"),
    user1.likes("Hop Butcher"),
    user1.is_senior(),
    user1.birthday(),
    User.active_users,
    user2.logout(),
    User.active_users
)

banner("""Continued…""")
# ------------------------------
class Pet:
    allowed = ["cat", "dog", "fish", "rat"]
    
    def __init__(self, name, species):
        # note: you don't have to reference as
        # Pet.allowed while in __init__ due to scope
        # if you're not using it elsewhere in the class,
        # i.e.:
        # if species not in allowed:
        if species not in Pet.allowed:
            raise ValueError(f"You can have a {species} pet.")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can have a {species} pet.")
        self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")
#tiger = Pet("Tony", "tiger")

banner("""
Showing that allowed is same 
in class as well as instances:
Pet.allowed, dog.allowed, cat.allowed
""")
# ------------------------------
print(id(Pet.allowed))
print(id(dog.allowed))
pl(id(cat.allowed))
print("This means self.allowed is legal. But not really apparent, best to do Class.attribute reference for clarity")

banner("""Exercise 79: Chicken Coop""")
# ------------------------------
class Chicken:
    
    total_eggs = 0

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0
    
    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs
