from modules.printutils import *
from random import randint

bannerline('basic loop')
for x in range(1, 10):
    print(x)

bannerline('expression in loop')
for x in range(1, 10):
    print(x * x)

bannerline('print letters in a string')
for letter in 'coffee':
    print(letter)

bannerline('print letters in a string, calculated')
for letter in 'coffee':
    print(letter * randint(1,10))