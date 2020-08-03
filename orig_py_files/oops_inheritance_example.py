from modules.printutils import *

big_banner("""
    OOPS: Inheritance Example, User & Moderator
    -------------------------------------------

    Based on reddit-style users.
""")

# base class

class User:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users online."

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out."

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]} {self.last[0]}"

    def likes(self, thing):
        return f"{self.first} likes {thing}."

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}!"


class Moderator(User):

    active_mods = 0

    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.active_mods} active moderators online."

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.active_mods += 1

    def remove_post(self):
        return f"{self.full_name()} removed a post from {self.community}."

u1 = User("Tom", "Garcia", 35)
u2 = User("Alfred", "Eisenstag", 58)
u3 = User("Billy", "Gnell", 22)
jasmine = Moderator("Jasmine", "O'Connor", 61, "Piano")
felix = Moderator("Felix", "Hanberstat", 44, "Wine")

print(User.display_active_users())
pl(Moderator.display_active_mods())

print(felix.logout())
print(User.display_active_users())
print(Moderator.display_active_mods())

