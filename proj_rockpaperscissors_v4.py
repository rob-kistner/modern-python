from random import randint
from modules.printutils import *

""" ----------------------------------------
    v4 Rock Paper Scissors

    Using random compter AI
---------------------------------------- """

# initialize scores & set globals
player_wins = 0
computer_wins = 0
num_wins = 3
els = ('rock', 'paper', 'scissors')

# loop through game until number of wins (num_wins)
# is reached
while player_wins < num_wins and computer_wins < num_wins:

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
    print(f'Player Score: {player_wins} / Computer Score: {computer_wins}')
    print('...rock...')
    print('...paper...')
    print('...scissors...')
    print('(against the computer)')

    bl()
    player = input('Player, make your move: ').lower()
    if player == 'q' or player == 'quit':
        bl()
        sep()
        break
    print(f'\nComputer plays: {computer}')

    # test tie
    if player == computer:
        banner('It\'s a tie!')
    # test logic
    elif player == 'rock':
        if computer == 'scissors':
            banner('Player 1 wins!')
            player_wins += 1
        elif computer == 'paper':
            banner('Computer wins!')
            computer_wins += 1
    elif player == 'paper':
        if computer == 'rock':
            banner('Player 1 wins!')
            player_wins += 1
        if computer == 'scissors':
            banner('Computer wins!')
            computer_wins += 1
    elif player == 'scissors':
        if computer == 'rock':
            banner('Computer wins!')
            computer_wins += 1
        if computer == 'paper':
            banner('Player 1 wins!')
            player_wins += 1
    # error catch
    else:
        banner('Something went wrong')
    sep()

# final win report
if player_wins != num_wins and computer_wins != num_wins:
    print('  Quitting early...')
elif player_wins > computer_wins:
    print('  CONGRATS, You\'re the winner!!!')
else:
    print('  The computer beat your behind this time.')
sep()
print('FINAL SCORE…')
print(f'  Player: {player_wins}')
print(f'  Computer: {computer_wins}')
