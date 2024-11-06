# We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice.
# Write 3 lines of code to switch the contents of the variables.
# You are not allowed to type the words "milk" or "juice".
# You are only allowed to use variables to solve this exercise.

# Exercise:
# glass1 = "milk"
# glass2 = "juice"

# Hint:
# Imagine you actually have a glass of milk and a glass of juice.
# How can you switch out the liquids in real life?

# Solution:
glass1 = "milk"
glass2 = "juice"

glassTemp = glass1
glass1 = glass2
glass2 = glassTemp

# Solution Explanation:
# If we have two physical glasses, and we wanted to switch out the contents.
# We would need to grab an extra glass! So the solution is to create a
# temporary variable to store the contents from one glass.
#
# temp = glass1
# By storing the contents of glass1 in the temp variable. We can now use the glass1 variable to store the contents of glass2
#
# glass1 = glass2
# Finally, we can put the contents in the temp variable into glass2.
#
# glass2 = temp
# Try it out with some physical glass cups!