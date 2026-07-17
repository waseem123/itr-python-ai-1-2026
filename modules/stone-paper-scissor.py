import random as r

mylist = ['stone','paper','scissor']

player1 = r.choice(mylist)
player2 = r.choice(mylist)

print(f'PLAYER 1 - {player1}')
print(f'PLAYER 2 - {player2}')

if player1 == player2:
    print('MATCH TIE')
elif player1=='stone' and player2=='scissor':
    print('PLAYER 1 WINS')
elif player1=='paper' and player2=='stone':
    print('PLAYER 1 WINS')
elif player1=='scissor' and player2=='paper':
    print('PLAYER 1 WINS')
else:
    print('PLAYER 2 WINS')