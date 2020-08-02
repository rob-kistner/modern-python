from modules.printutils import *

big_banner("""
    OOPS: Creating a Grumpy Dict
    -------------------------------------
""")

# inherit from dict
class GrumpyDict(dict):

    def __repr__(self):
        print("NONE OF YOUR BUSINESS!")
        return super().__repr__()
    
    # override
    def __missing__(self, key):
        return f"YOU WANT {key.upper()}? WELL IT AIN'T HERE!"

    # override
    def __setitem__(self, key, value):
        print(f"YOU WANT TO CHANGE THE DICTIONARY?")
        print(f"OK FINE…")
        super().__setitem__(key, value)
        print(super().__repr__())

    def __contains__(self, item):
        print("IT AIN'T HERE, DAMMIT!")
        return False

data = GrumpyDict({"first": "Tom", "animal": "Cat"})
pl(data)
pl(data['city'])
data['city'] = "San Francisco"
pl('sidewalk' in data)