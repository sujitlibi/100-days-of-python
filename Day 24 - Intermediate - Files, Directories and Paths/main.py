
# Need to close file
# file = open("my_text.txt")
# contents = file.read()
# print(contents)
# file.close()


# No need to close file using "witb" keyword function
# with open("my_text.txt") as file:
#     contents = file.read()
#     print(contents)


with open("my_text.txt", mode="a") as file:
    file.write("\nAdd this line of text")