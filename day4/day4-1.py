from random import randint
from ascii import rock, paper, scissors
import sys
game_images = [rock,paper,scissors]
user_input = input('hey, welcome to RPS, chose between rock, paper, scissors : ').lower()
computer_input = randint(0,2)


print('you chose : \n', )
if user_input == 'rock':
    user_input = 0
elif user_input == 'paper':
    user_input = 1
elif user_input == 'scissors':
    user_input = 2
else:
    print('invalid input ! ')
    sys.exit()

if user_input>=0 and user_input<=2:
    print(game_images[user_input])

print('Computer chose : \n', )
print(game_images[computer_input])


if computer_input == user_input:
    print('it\'s a tie, try again')
elif computer_input ==0 and user_input == 1:
    print('you won')
elif computer_input ==1 and user_input == 2:
    print('you won')
elif computer_input ==2 and user_input == 0:
    print('you won')
else:
    print('computer won')
