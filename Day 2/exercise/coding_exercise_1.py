# Coding Challenge:
# BMI Calculator
# The body mass index (BMI) is a measure used in medicine to see if someone
# is underweight or overweight. This is the formula used to calculate it:
#
# bmi is equal to the person's weight divided by the person's height squared.
#
# Convert this sentence into code on line 6.

# Hint:
# For the tests to pass you need to keep the height and weight the same as the starting code.
# height = 1.65
# weight = 84
# You need to calculate the squared height first.

# Solution:
height = 1.65
weight = 84
# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)
print(bmi)