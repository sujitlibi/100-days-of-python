# Instruction
# Dictionary Comprehension 1
# You are going to use Dictionary Comprehension to create a dictionary called
# result that takes each word in the given sentence and calculates the number
# of letters in each word.
#
# Try Googling to find out how to convert a sentence into a list of words.  *
#
# *Do NOT** Create a dictionary directly.
#
# Try to use Dictionary Comprehension instead of a Loop.
#
#
#
# To keep this exercise simple, count any punctuation following a word with no
# whitespace as part of the word. Note that "Swallow?" therefore has a length of 8.

# Solution
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list_word = sentence.split()

result = {word: len(word) for word in list_word}
print(result)
