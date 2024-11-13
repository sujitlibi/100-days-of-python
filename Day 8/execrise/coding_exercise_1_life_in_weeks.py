# Life in Weeks
# I was reading this article by Tim Urban -
# Your Life in Weeks and realised just how little time we actually have.
#
# Create a function called life_in_weeks()
# using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
#
# It will take your current age as the input and output a message with our time left in this format:
#
# You have x weeks left.
#
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
#
#
#
# **Warning** The function must be called life_in_weeks for the tests to pass.
# Also the output must have the same punctuation and spelling as the example.
# Including the full stop!
#
# Example Input
#
# 56
#
# Example Output
#
# You have 1768 weeks left.
#
# How to test your code and see your output?

# Udemy coding exercises do not have a console, so you cannot use input() .
# You will need to call your function with hard-coded values like so:

# def life_in_weeks(age):
  # your code here

# Call your function with hard coded values
# life_in_weeks(12)

# Solution
def life_in_weeks(current_age):
    total_year = 90
    total_week_in_90_year = 90 * 52
    current_age_in_week = current_age * 52 # there are around 52 weeks in one year
    remaining_time_in_week = total_week_in_90_year - current_age_in_week
    print(f"You have {remaining_time_in_week} weeks left.")


life_in_weeks(56)

# Hint
# Make sure you define your function as  life_in_weeks() .
# Also make sure you print out in this exact format: You have X weeks left.
# There are 52 weeks in a year.

# Angela Solution

# def life_in_weeks(age):
#     years_remaining = 90 - age
#     weeks_remaining = years_remaining * 52
#     print(f"You have {weeks_remaining} weeks left.")
#
# life_in_weeks(12)