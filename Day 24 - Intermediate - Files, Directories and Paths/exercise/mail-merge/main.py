#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open("./Input/Names/invited_names.txt") as file:
    invited_name = file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.readlines()

for name in invited_name:
    updated_letter_content = letter_contents[0].replace("[name]", name.strip("\n"))
    updated_letter = [updated_letter_content] + letter_contents[1:]
    with open(f"./Output/ReadyToSend/letter_to_{name.strip("\n")}.txt", mode="w") as letter:
        for content in updated_letter:
            letter.write(content)