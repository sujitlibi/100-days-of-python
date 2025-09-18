# List Comprehension

# Syntax:
# new_lists = [new_item for item in list]

# Tradition Approach
# numbers = [1,2,3]
# new_lists = []
# for n in numbers:
#   add_one = n + 1
#   new_lists.append(add_one)

# Using List Comprehension
numbers = [1,2,3]
new_lists = [n+1 for n in numbers]

# List Comprehension not only suppose to work with list only but work with other as well for example
name = "Sujit Kumar Libi"
new_list = [letter for letter in name]

# Challenge: Create a new list from range, where the list items are double the values in the range
double_value = [num * 2 for num in range(1,5)]
print(double_value)

# Conditional List Comprehension
# Syntax:
# new_list = [new_item from item in list if test_condition]

# Example:
names = ["Sujit", "Sumit", "Subarna", "Ram", "Shyam"]
short_name = [name for name in names if len(name) < 5]
print(short_name)

uppercase_name = [name.upper() for name in names if len(name) > 5]
print(uppercase_name)
