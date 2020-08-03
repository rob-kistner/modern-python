from modules.printutils import *

big_banner("""
    OOPS: Properties
    ----------------
    Prevents users from doing dumb things
    to class members.

    NOTE: the _variable standard is largely based 
    on respect between developers. You can always 
    just access it by setting _variable = "value" but
    you're just "not supposed to do that".
""")

class Human:
    def __init__( self, first, last, age ):
        self.first = first
        self.last = last
        # implied private member
        self._age = max(age, 0)

    # you could use setters/getters like…

    # def get_age( self ):
    #     return self._age

    # def set_age( self, age ):
    #     self._age = max(age, 0)

    # @property decorator means you
    # can call the member without using
    # a function getter like above
    @property
    def age( self ):
        return self._age
    
    # @<member>.setter decorator means you
    # can set the member value without using
    # a function setter like above
    @age.setter
    def age( self, value ):
        self._age = max(value, 0)
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    # this would work but it's risky
    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(" ")

jane = Human("Jane", "Goodall", 50)

expected(
    "jane.age",
    jane.age
)

jane.age = 34
expected(
    "jane.age = 34",
    jane.age
)

jane.age = -20
expected(
    "jane.age = -20",
    jane.age
)

expected(
    "jane.fullname",
    jane.fullname
)

jane.fullname = "Rob K"
expected(
    "jane.fullname = 'Rob K'",
    jane.fullname
)
print(jane.__dict__)