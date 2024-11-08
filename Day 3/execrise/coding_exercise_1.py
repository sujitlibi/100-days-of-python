# BMI Calculator with Interpretations
# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
#
# If the bmi is under 18.5 (not including), print out "underweight"
#
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
#
# If the bmi is 25 (including) or over, print out "overweight"
#
# Refer to this graphic for help:

weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5:
    print("normal weight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")

# Hint:
# In the code below, B is between 10 (including) and 20 (not including).
#
# if n >= 20:
#     A
# elif n >= 10:
#     B
# else:
#     C

# Solution Explanation:

# weight = 85
# height = 1.85
#
# bmi = weight / (height ** 2)
#
# if bmi >= 25:
#     print("overweight")
# elif bmi >= 18.5:
#     print("normal weight")
# else:
#     print("underweight")
#
# If bmi greater than or equal to 25, it will print "overweight".
#
# If the first check is true, the code will stop running, but if the first
# condition was false then it will make the next elif check to see if it's
# greater than or equal to 18.5. So if it's not greater than 25, and it's
# greater than 18.5 then the 18.5-25 range will print "normal weight".
#
# Everything else will be below 18.5 and that will print "underweight".
