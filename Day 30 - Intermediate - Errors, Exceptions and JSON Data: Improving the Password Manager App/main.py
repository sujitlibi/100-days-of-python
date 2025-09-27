# FileNotFound
# with open("password.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Cherry"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# Catch Exception: Explanation
# try:
#   Something that might cause an exception
# except:
#   Do this if there was an exception
# else:
#   Do this if there were no exceptions
# finally:
#   Do this no matter what happens

# Example 1:

# try:
#     file = open("book.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["non_existent"])
# except FileNotFoundError:
#     file = open("book.txt", "w")
#     file.write("Alpha")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File has been closed.")
#     raise TypeError("This is an error that I made up.")


# Example 2:

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should be less than 3 meters.")

bmi = weight / height ** 2
print(bmi)