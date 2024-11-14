print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TreasureHunt]
*******************************************************************************
''')
print('hii, welcome to treasure island')
left_or_right = input('you\'re at a cross road, which direction you want to take? "left" or "right" : \n').lower()

if left_or_right == 'left':
    swim_or_wait = input('now, you reached at the bank of river, now either you'
' can wait for a boat, or you can swim, chose between "walk" or "swim" : \n').lower()
    if swim_or_wait =='walk':
        three_door = input('now, you reached at the island and there are 3 doors: "red", "green", "blue", chose between one of them : ').lower()
        if three_door =='green':
            print('you won!')
        else:
            print('Game Over')
    else:
       print('you fell into a hall, and it\'s game over')
elif left_or_right =='right':
    print('you fell into a hall, and it\'s game over')
else:
    print('invalid input')


print('thanks for playing Treasure Hunt python')