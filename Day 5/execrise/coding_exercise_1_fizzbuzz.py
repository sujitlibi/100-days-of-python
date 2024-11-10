# FizzBuzz
# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
# e.g. it might start off like this:
#
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# ...etc

# Solution:
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# Hint

# - Remember your answer should start from 1 and go up to and including 100.
#
# - Each number/text should be printed on a separate line.
#
# - Remember on Day 3, you learnt to use the modulo operator %
# to check if a number is odd or even. You will need to use the same
# concept to check if a number is divisible by 3 or by 5.
#
# e.g.
#
# number = 12
# if number % 3 == 0:
#     print("number is divisible by 3")


# Solution Explanation

# Create a loop with For and Range to go from 1 to 100.
# for number in range(1, 101):
#     # First check if the number is divisible by both 3 and 5.
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#
#     # Then check if the number is only divisible by 3
#     elif number % 3 == 0:
#         print("Fizz")
#
#     # Finally check if the number is only divisible by 5
#     elif number % 5 == 0:
#         print("Buzz")
#
#     # If it's not divisible by either of those numbers, just print the number
#     else:
#         print(number)
