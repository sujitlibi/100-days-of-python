# Coding Exercise:

# Instruction
# Grading Program
# You have access to a database of student_scores in the format of a dictionary.
# The keys in student_scores are the names of the students and
# the values are their exam scores.
#
# Write a program that converts their scores to grades.
#
# By the end of your program, you should have a new dictionary
# called student_grades that should contain student
# names as keys and their assessed grades for values.
#
# The final version of the student_grades dictionary will be checked.
#
# **DO NOT** modify lines 1-7 to change the existing student_scores dictionary.
#
# This is the scoring criteria:
#
# - Scores 91 - 100: Grade = "Outstanding"
# - Scores 81 - 90: Grade = "Exceeds Expectations"
# - Scores 71 - 80: Grade = "Acceptable"
# - Scores 70 or lower: Grade = "Fail"

# Hint
# Remember that looping through a Dictionary will only give you the keys and not the values.
# - If in doubt as to why your code is not doing what you expected,
# you can always print out the intermediate values.

# My Solution
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student_name in student_scores:
    if student_scores[student_name] >= 91:
        student_grades[student_name] = "Outstanding"
    elif student_scores[student_name] >= 81 and student_scores[student_name] <= 90:
        student_grades[student_name] = "Exceeds Expectations"
    elif student_scores[student_name] >= 71 and student_scores[student_name] <= 80:
        student_grades[student_name] = "Acceptable"
    else:
        student_grades[student_name] = "Fail"

print(student_grades)

# Angela Solution / Explanation

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
#
# # Create an empty dictionary to collect the new values.
# student_grades = {}
#
# # Loop through each key in the student_scores dictionary
# for student in student_scores:
#
#     # Get the value (student score) by using the key each time.
#     score = student_scores[student]
#
#     # Check what grade the score would get, then add it to student_grades
#     if score >= 91:
#         student_grades[student] = 'Outstanding'
#     elif score >= 81:
#         student_grades[student] = 'Exceeds Expectations'
#     elif score >= 71:
#         student_grades[student] = 'Acceptable'
#     else:
#         student_grades[student] = 'Fail'
