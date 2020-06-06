from printutils import *

bl()

print('...rock...')
print('...paper...')
print('...scissors...')

bl()

player1 = input('Player 1: make your move: ')
player2 = input('Player 2: make your move: ')

result = ''

def showRes(s):
    print('\n' + s)


    # test logic
if player1 == 'rock' and player2 == 'scissors':
    showRes('Player 1 wins!')
elif player1 == 'rock' and player2 == 'paper':
    showRes('Player 2 wins!')
elif player1 == 'paper' and player2 == 'rock':
    showRes('Player 1 wins!')
elif player1 == 'paper' and player2 == 'scissors':
    showRes('Player 2 wins!')
elif player1 == 'scissors' and player2 == 'rock':
    showRes('Player 2 wins!')
elif player1 == 'scissors' and player2 == 'paper':
    showRes('Player 1 wins!')
    
    # catches
elif player1 == player2:
    showRes('It\'s a tie!')
else:
    showRes('Something went wrong')
