from modules.printutils import *

nums = [1, 2, 3]

print([x*.5 for x in nums])

name = 'colt'
print([char.upper() for char in name])

friends = ['ashley', 'matt', 'michael']
friends_upper = [(friend[0].upper() + friend[1:]) for friend in friends]
print(friends_upper)

comp = [num*10 for num in range(1,6)] 
print(comp)

comp = [bool(val) for val in [1, [], '']]
print(comp)

comp = [str(num) for num in [1,2,3,4,5]]
print(comp)