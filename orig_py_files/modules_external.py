from modules.printutils import *

big_banner("""
    External Modules
    ----------------

    * Built-in modules come with Python
    * External modules come from the internet
    * Install using pip

as of Python 3.4, pip comes installed with Python

You can run it (if it's not setup in your path) with:

    python3 -m pip install <package_name>

""")

# python3 -m pip install termcolor
import termcolor as tc

banner("""Running help on the termcolor package""")
# ------------------------------
#help(tc)


banner("""Experiments with termcolor""")
# ------------------------------
txt = tc.colored('Hi There', color="yellow")
print(txt)

txt = tc.colored('Hi There', color="white", on_color="on_red")
print(txt)

txt = tc.colored('Hi There', "cyan", "on_magenta")
print(txt)