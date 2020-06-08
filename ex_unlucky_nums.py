max = 20

# A clear method, assigning reply to a variable
# then compiling a print statement at the end...
# the conditionals are shorter/cleaner this way
#
for n in range(1, max+1):
    if n==4 or n==13:
        state = 'UNLUCKY!!!'
    elif n % 2 != 0:
        state = 'odd'
    # could just be else, but this is more clear
    elif n % 2 == 0:
        state = 'even'
    print('{} is {}'.format(n, state))