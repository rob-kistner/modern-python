from modules.printutils import *

numbers = [4,6,2,9,7,10]
colors = ['purple', 'teal', 'magenta', 'crimson', 'emerald']


banner('The lists...')
# ----------------------------------------
var_dump('numbers', numbers)
var_dump('colors', colors)


banner('For list')
# ----------------------------------------
for num in numbers:
    print(num)

print()

for color in colors:
    print(color)

print()

for num in numbers:
    print(num*2)


banner('While loop')
# ----------------------------------------
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

print()

index = 0
while index < len(colors):
    print(f"{index}: {colors[index]}")
    index += 1


banner('Exercise...')
# ----------------------------------------
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Define your code below:
result = ''
idx = 0
while idx < len(sounds):
    result += sounds[idx]
    idx +=1
print(result.upper())