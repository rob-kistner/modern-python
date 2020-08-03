from modules.printutils import *

big_banner("""
    OOPS: super()
    ----------------
    
""")


class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self, sound):
        print(f"This animal says {sound}")

    def __repr__(self):
        return f"{self.name} is a {self.species}"


class Cat( Animal ):

    def __init__(self, name, breed, toy):
        # this works, but why…
        # Animal.__init__(self, name, species)
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        return f"Cutie patootie {self.name} plays with {self.toy}."

# ----------------------------------------

blue = Cat("Blue", "Scottish Fold", "String")

expected(
    "printing the instance",
    blue
)

expected(
    "blue's members…",
    blue.name,
    blue.species,
    blue.breed,
    blue.toy
)

expected(
    "calling the Cat play() method",
    blue.play()
)