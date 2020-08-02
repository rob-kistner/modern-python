from modules.printutils import *

tasks = ['a', 1, 45, True, 6.778]

banner('Getting list length with len()')
# ----------------------------------------
print(len(tasks))

banner('Turning a range into a list')
# ----------------------------------------
r = list(range(1, 10))
print(r)