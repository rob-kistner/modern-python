from modules.printutils import *

big_banner("""
    OOPS: Creating Classes
    ----------------------
    Convention for naming: camelcase
""")


class User:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


user1 = User("Joe", "Smith", 19)
user2 = User("Blanca", "Lopez", 34)

print(user1.firstname, user1.lastname)
print(user2.firstname, user2.lastname)


banner("""Exercise 77""")
# ------------------------------

class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes

    # adding some testing methods
    
    def get_likes(self):
        return f"👍 {self.likes}"

    def show_comment(self):
        print(f"\"{self.text}\"")
        print(f"{self.username} • {self.get_likes()}")
        print()


# create the objects
comment1 = Comment("resa777", "soooo cute!!!", likes=8)
comment2 = Comment("billw7", "hating on this")
comment3 = Comment("andifinour", "Why is this so relevant? Asking for a friend", likes=2)

# show comments
comment1.show_comment()
comment2.show_comment()
comment3.show_comment()
