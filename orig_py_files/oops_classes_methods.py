from modules.printutils import *

big_banner("""
    OOPS: Creating Instance Methods
""")


class User:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

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
    user1.birthday()
)


big_banner("""
    Class Methods
    -------------

    Not concerned with individual instances, 
    but rather the class itself. They use 
    the @classmethod decorator.
""")
# ------------------------------

class Person:

    active_users = 0

        # note how we're passing the actual class
        # into the classmethod: cls
    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} Persons"

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        Person.active_users += 1

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

rob = Person("Rob", "Kistner", 50)
jenny = Person("Jenny", "Miller", 51)
marjan = Person("Marjan", "Samadi", 38)
cindy = Person("Cindy", "Xiong", 25)
glenn = Person("Glenn", "Chipman", 40)
pl(
    Person.display_active_users()
)