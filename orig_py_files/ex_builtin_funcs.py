from modules.printutils import *


def max_magnitude(nums):
    return max(abs(num) for num in nums)

output = max_magnitude([50,300,-400])
print(output)


def sum_even_values(*nums):    
    """
    Add & return even values only
    """
    return sum(num for num in nums if num%2==0)

output = sum_even_values(5,1,2,9,4,8,3)
print(output)


def sum_floats(*args):
    """
    Add & return float values only
    """
    return sum(arg for arg in args if type(arg) == float)

output = sum_floats(1.5, 2.4, 'awesome', [], 1)
print(output)