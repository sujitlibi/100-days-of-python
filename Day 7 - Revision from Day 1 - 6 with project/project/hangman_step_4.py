# TODO-1:
# Create a variable called lives to keep track of the number of lives left.
# Set lives to equal 6.
# TODO-2:
# If guess is not a letter in the chosen_word, Then reduce lives by 1.
# If lives goes down to 0 then the game should end, and it should print "You lose."
#  Hint
# The not in keywords will be your friend in this todo.
#  You can check if something exists in the chosen_word completely separately from the rest of the code.

# TODO-3:
# print the ASCII art from the list stages that corresponds to the current number of lives the user has remaining.

import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.

chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1

    print(stages[lives])

    print(f"Remaining lives: {lives}")
    # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."

    if "_" not in display:
        game_over = True
        print("You win.")

    if lives == 0:
        game_over = True
        print("You Lose. Game Over.")

    # TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.
