import pandas

nato_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your name: ").upper()

phonetic_code = {letter: nato_dict[letter] for letter in user_input}
print(phonetic_code)