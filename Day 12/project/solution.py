# The goal is to build a guess the number game.
#
# Demo
# https://appbrewery.github.io/python-day12-demo/
#
# ASCII Art
# You can get hold of ASCII art using the link below:
# https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

# My Solution

import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

secret_num = random.randint(1, 100)
level = input("Choose a difficulty. Type 'easy' or 'hard':")

user_lives = EASY_LEVEL_ATTEMPTS if level == 'easy' else HARD_LEVEL_ATTEMPTS

def guess(remaining_live):
    print(f"You have {remaining_live} attempts remaining to guess the number")
    guess_num = int(input("Make a guess:"))
    return guess_num

while user_lives > 0:
    guessed_num = guess(user_lives)
    if guessed_num is secret_num:
        print(f'You got it! The answer was {secret_num}')
        break
    user_lives -= 1
    if user_lives == 0:
        print("You've run out of guesses. Refresh the page to run again")
        break
    print('Too High' if guessed_num > secret_num else 'Too Low')
    print("Guess Again")

# Angela Solution:

# from random import randint
# from art import logo
#
#
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5
#
#
# # Function to check users' guess against actual answer
# def check_answer(user_guess, actual_answer, turns):
#     """Checks answer against guess, returns the number of turns remaining."""
#     if user_guess > actual_answer:
#         print("Too high.")
#         return turns - 1
#     elif user_guess < actual_answer:
#         print("Too low.")
#         return turns - 1
#     else:
#         print(f"You got it! The answer was {actual_answer}")
#
#
# # Function to set difficulty
# def set_difficulty():
#     level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS
#
#
# def game():
#     print(logo)
#     # Choosing a random number between 1 and 100.
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#     answer = randint(1, 100)
#     print(f"Pssst, the correct answer is {answer}")
#
#     turns = set_difficulty()
#
#     # Repeat the guessing functionality if they get it wrong.
#     guess = 0
#     while guess != answer:
#         print(f"You have {turns} attempts remaining to guess the number.")
#         # Let the user guess a number
#         guess = int(input("Make a guess: "))
#         # Track the number of turns and reduce by 1 if they get it wrong
#         turns = check_answer(guess, answer, turns)
#         if turns == 0:
#             print("You've run out of guesses, you lose.")
#             return
#         elif guess != answer:
#             print("Guess again.")
#
# game()


