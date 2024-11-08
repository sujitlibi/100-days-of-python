print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Your goal today is to build a "Chose your own adventure game".
# Using what you have learnt in the lessons today you will be
# building a very simple version of this type of text game.
#
# Use the flow chart linked here to create the game logic.
#
# Once you've completed the project, you can always extend
# the game and make it more interesting!


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

cross_road = input("You're at a cross road. "
                   "Where do you want to go?\n"
                   " \tType \"left\" or \"right\": \n").lower()
if cross_road == 'left':
    lake = input("You've come to a lake. "
                 "There is an island in the middle of the lake.\n "
                 "\tType \"wait\" to wait a boat. "
                 "Type \"swim\" to swim across.\n").lower()
    if lake == 'wait':
        door_color = input("You arrive at the island unharmed. "
                           "There is a house with 3 door.\n "
                           "\tOne red, one yellow and one blue. "
                           "Which color do you choose?\n").lower()
        if door_color == 'red':
            print("Burned by fire!!!\n "
                  "GAME OVER!!!")
        elif door_color == 'blue':
            print("Eaten by beasts!!!\n "
                  "GAME OVER!!!")
        elif door_color == 'yellow':
            print("YOU WON!!!!!!!!!!!!!")
        else:
            print("GAME OVER!!!")
    else:
        print("Attacked by trout!!!\n "
              "GAME OVER!!!")
else:
    print("Fall into a hole!!!\n "
          "GAME OVER!!!")
