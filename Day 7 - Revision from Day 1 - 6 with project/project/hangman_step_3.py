# TODO-1
# Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word.
# At that point display has no more blanks ("_"). Then you can tell the user they've won.
#  Hint 1
# You can use the in keyword to check if a String or List contains a particular item.
# e.g. Google: check if a letter is present in a string python
#
# TODO-2
# Update the for loop so that previous guesses are added to the display String.
# At the moment, when the user makes a new guess, the previous guess gets replaced by a "_".
# We need to fix that by updating the for loop.
#  Hint 2
# Think about how you can store the matched letters and use an elif to check if a letter has been matched before.

import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
game_over = False
correct_letters = []
while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    # TODO-2: Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
    if "_" not in display:
        game_over = True
        print("You win!!!!")