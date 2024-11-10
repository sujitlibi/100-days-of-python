import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_list = [rock, paper, scissors] # [0: rock, 1: paper, 2: scissor]

user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissor\n"))

computer_choose = random.randint(0,2)

if user_choose == 1 or user_choose == 2 or user_choose == 0: # user_choose >= 0 and user_choose < 3
    print(game_list[user_choose])
    print("Computer Choose\n")
    print(game_list[computer_choose])
    if user_choose == computer_choose:
        print("Both select same. Its draw")
    else:
        if (user_choose == 0 and computer_choose == 1) or (user_choose == 1 and computer_choose == 2) or (user_choose == 2 and computer_choose == 0):
            print("You Lose!!!")
        if (user_choose == 0 and computer_choose == 2) or (user_choose == 1 and computer_choose == 0) or (user_choose == 2 and computer_choose == 1):
            print("You Win!!!")
else:
    print("Please select valid input only. Restart you game again.")
