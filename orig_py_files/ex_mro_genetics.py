from modules.printutils import *

big_banner("""
    Exercise 82: MRO Genetics
""")


class Mother:

    # dominant traits
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"

class Father:

    # recessive traits
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"

class Child(Mother, Father):
    
    def __init__(self):
        super().__init__()


billy = Child()

pl(billy.eye_color)
pl(billy.hair_color)
pl(billy.hair_type)