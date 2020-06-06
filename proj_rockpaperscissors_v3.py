from random import randint
from modules.printutils import *

""" ----------------------------------------
    v3 Rock Paper Scissors

    Using random compter AI
---------------------------------------- """

# globals
els = ('rock', 'paper', 'scissors')

# get computer's random turn
rand_num = randint(1, 3)

if rand_num == 1:
    computer = 'rock'
elif rand_num == 2:
    computer = 'paper'
else:
    computer = 'scissors'

# shorter solution: could also do...
#
#   computer = els[randint(0, 2)]

bl()
print('...rock...')
print('...paper...')
print('...scissors...')
print('(against the computer)')

bl()
player = input('Player, make your move: ').lower()
print(f'\nComputer plays: {computer}')

# test tie
if player == computer:
    printsurround('It\'s a tie!')

# test logic
elif player == 'rock':
    if computer == 'scissors':
        printsurround('Player 1 wins!')
    elif computer == 'paper':
        printsurround('Computer wins!')
elif player == 'paper':
    if computer == 'rock':
        printsurround('Player 1 wins!')
    if computer == 'scissors':
        printsurround('Computer wins!')
elif player == 'scissors':
    if computer == 'rock':
        printsurround('Computer wins!')
    if computer == 'paper':
        printsurround('Player 1 wins!')

# catch
else:
    printsurround('Something went wrong')
