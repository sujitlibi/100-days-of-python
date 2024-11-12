# Your goal is to build a Hangman game using
# everything you have learnt about Python programming.
#
# Demo Final Project
# https://appbrewery.github.io/python-day7-demo/
#
# The project is split into 5 major steps.
# In each step, there will be multiple TODOs.
# Your goal is to go through each todo in order and complete them.
#
# You can view all the todos easily in
# PyCharm by going to View -> Tool Windows -> TODOs
#
# TODO-1
# Randomly choose a word from the word_list
# and assign it to a variable called chosen_word. Then print it.
#
# TODO-2
# Ask the user to guess a letter and assign
# their answer to a variable called guess.
# Make the String stored in guess lowercase.
#
# TODO-3
# Check if the letter the user guessed guess
# is one of the letters in the chosen_word.
# Loop through each of the letters in the chosen_word
# and print "Right" if the letter is a match, "Wrong" if it's not.
#

import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list
#  and assign it to a variable called chosen_word.
#  Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)
# TODO-2 - Ask the user to guess a letter and assign
#  their answer to a variable called guess.
#  Make guess lowercase.
guess = input("Guess a letter:\n").lower()

# TODO-3 - Check if the letter the user guessed (guess)
#  is one of the letters in the chosen_word.
#  Print "Right" if it
#  is, "Wrong" if it's not.
for char in chosen_word:
    if char == guess:
        print("Right")
    else:
        print("Wrong")

