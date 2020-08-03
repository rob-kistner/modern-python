from modules.printutils import *

big_banner("""
    OOPS: Class Methods Advanced
""")

class User:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} Users."

        # this will create a new instance based on
        # the data in a comma-separated string
    @classmethod
    def from_string(cls, datastr):
        firstname, lastname, age = datastr.split(",")
        return cls(firstname, lastname, int(age))
 
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

rob = User.from_string("Rob,Kistner,50")
jenny = User.from_string("Jenny,Miller,51")

pl(
    rob.fullname(),
    jenny.fullname(),
    User.display_active_users()
)