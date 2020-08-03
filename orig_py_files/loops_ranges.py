from modules.printutils import *
from random import randint

banner('basic range')
for num in range(1, 10):
	print(num)

banner('basic range without starting value')
for num in range(5):
	print(num)

banner('range: skipping')
for num in range(10, 22, 2):
	print(num)