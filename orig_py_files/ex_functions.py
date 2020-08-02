from modules.printutils import *


def return_day(day_num):
    """
    return the day of the week passed as an integer 1-7
    """
    days_of_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    if day_num < 1 or day_num > 7:
        return None
    else:
        return days_of_week[day_num-1]

print(return_day(3))

"""
Looking ahead to try/except, 
you could also write the above as…

def return_day(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None
"""

sep()

def last_element(l):
    """
    return last element of a list
    """
    if l:
        return l[-1]
    return None

print(last_element([1,2,3,4]))


sep()

def number_compare(a,b):
    """
    return "First is greater" if the first param
    is greater than the second, return "Second is greater"
    if the second is greater than the first. Return 
    "Numbers are equal" if they're equal
    """
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"

print(number_compare(7,10))
print(number_compare(4,2))
print(number_compare(5,5))

sep()

def single_letter_count(s1, s2):
    '''
    return how many times the 2nd param occurs 
    in the first param
    '''
    return s1.lower().count(s2.lower())


print(single_letter_count("hello", "h"))


sep()

def multiple_letter_count(string):
    """
    return a dict of keys(letters in a string) in 
    values(count of that letter in a string)
    """
    return {letter: string.count(letter) for letter in string}


print(multiple_letter_count('willow'))


sep()

def list_manipulation(thelist, cmd, loc, theval=None):
    '''
    list_manipulation([1,2,3], "remove", "end") # 3
    list_manipulation([1,2,3], "remove", "beginning") #  1
    list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
    list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
    '''
    if cmd == "remove":
        if loc == "beginning":
           return thelist.pop(0)
        return thelist.pop()
    elif cmd == "add":
        if loc == "beginning":
            thelist.insert(0, theval)
        else:
            thelist.append(theval)
        return thelist
print(list_manipulation([1,2,3], "remove", "end"))
print(list_manipulation([1,2,3], "remove", "beginning"))
print(list_manipulation([1,2,3], "add", "beginning", 20))
print(list_manipulation([1,2,3], "add", "end", 30))


sep()

def is_palindrome(word):
        # remove whitespace for good measure
    wordclean = word.replace(" ", "").lower()
    return wordclean == wordclean[::-1]

print(is_palindrome('Hannah'))
print(is_palindrome('blake'))


sep()

def frequency(thelist, search):
    return thelist.count(search)

print(frequency([1,2,3,4,3,31,2], 3))


sep()

def multiply_even_numbers(lst):
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total

print(multiply_even_numbers([1,2,3,4,5,6]))


sep()

def capitalize(word):
    return word[0:1].upper() + word[1:].lower()

print(capitalize('aardvark'))


sep()

def compact(thelist):
    return [item for item in thelist if item]


print(compact([0,1,2,"",[],False,{},None,"All done"]))


sep()

def intersection(list1, list2):
    return [item for item in list1 if item in list2]

print(intersection([1,2,3], [3,4,5]))
