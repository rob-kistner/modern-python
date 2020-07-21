from modules.printutils import *


def max_magnitude(nums):
    return max(abs(num) for num in nums)

print(max_magnitude([50,300,-400]))


def sum_even_values(*nums):    
    return sum(num for num in nums if num%2==0)

print(sum_even_values(5,1,2,9,4,8,3))


def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)

print(sum_floats(1.5, 2.4, 'awesome', [], 1))