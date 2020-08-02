from modules.printutils import *

banner("""
    Using the keyword <function>.__doc__ will show
    the docstring definied in a function. It's important to
    define it at the top of the function
""")

def say_hello():
    # note the spacing, it's absolute to what you 
    # put in the docstring
    """
    A simple function to say hello.
    It'll obey all the formatting you 
    put in the string itself including
    spaces at the beginning.
    """
    return "Hello!"

print(say_hello.__doc__)

sep()

print([].pop.__doc__)