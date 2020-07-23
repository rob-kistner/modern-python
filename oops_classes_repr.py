from modules.printutils import *

big_banner("""
    OOPS: repr
""")

class User:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} Users."

    @classmethod
    def from_string(cls, datastr):
        firstname, lastname, age = datastr.split(",")
        return cls(firstname, lastname, int(age))
 
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        User.active_users += 1

        # you can just print(<instance name>) to
        # run this method
    def __repr__(self):
        props = (
            "User:",
            "-----",
            f"{self.firstname} {self.lastname}",
            f"{self.firstname} is {self.age} years old"
        )
        return "\n".join(props)

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
    rob,
    jenny
)