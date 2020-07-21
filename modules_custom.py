from modules.printutils import *

banner("custom modules")
# ----------------------------------------
import modules_custom_bananas as bananas
import modules_custom_apples as apples
    # ugly, but allows you to alias a bunch of function aliases
from modules_custom_bananas import \
    dipped_in_chocolate as dip

print(bananas.dipped_in_chocolate())
print(dip())
print(apples.offer())