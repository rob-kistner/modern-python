from modules.printutils import *

""" ----------------------------------------
    v2 Rock Paper Scissors

    Refactored from the clumsy nested if
    statements in version 1 with...well...
    some even clumsier nested if's that is 
    less code
---------------------------------------- """

def showRes(s):
    print('\n' + s + '\n')

bl()

print('...rock...')
print('...paper...')
print('...scissors...')

bl()
player1 = input('Player 1: make your move: ')
player2 = input('Player 2: make your move: ')

    # test tie
if player1 == player2:
    showRes('It\'s a tie!')

    # test logic
elif player1 == 'rock':
    if player2 == 'scissors':
        showRes('Player 1 wins!')
    elif player2 == 'paper':
        showRes('Player 2 wins!')
elif player1 == 'paper':
    if player2 == 'rock':
        showRes('Player 1 wins!')
    if player2 == 'scissors':
        showRes('Player 2 wins!')
elif player1 == 'scissors':
    if player2 == 'rock':
        showRes('Player 2 wins!')
    if player2 == 'paper':
        showRes('Player 1 wins!')
    
    # catch
else:
    showRes('Something went wrong')
