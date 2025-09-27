
# Challenge 3:
# Catch the KeyError when a user enters a character that is not in the dictionary
# Provide feedback to the user when an illegal word was entered.
# Continue prompting the user to enter another word until they enter a valid word
# Error Message: "Sorry, only letters in the alphabet please."
import pandas

nato_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# Solution 1: Using While Loop

# while True:
#     user_input = input("Enter your name: ").upper()
#
#     # If we want to show it on dictionary
#     # phonetic_code = {letter: nato_dict[letter] for letter in user_input}
#     # print(phonetic_code)
#
#     # If we want to show it on list
#     try:
#         phonetic_code = [nato_dict[letter] for letter in user_input]
#     except KeyError as error_message:
#         print(f"Sorry, only letters in the alphabet please.")
#         continue
#     else:
#         print(phonetic_code)
#         break

# Solution 2: using recursion function

def generate_phonetic_code():
    user_input = input("Enter your name: ").upper()

    # If we want to show it on dictionary
    # phonetic_code = {letter: nato_dict[letter] for letter in user_input}
    # print(phonetic_code)

    # If we want to show it on list
    try:
        phonetic_code = [nato_dict[letter] for letter in user_input]
    except KeyError as error_message:
        print(f"Sorry, only letters in the alphabet please.")
        generate_phonetic_code()
    else:
        print(phonetic_code)

generate_phonetic_code()