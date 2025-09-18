# How to use dictionary comprehension

# Syntax:
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items()}
# new_dict = {new_key: new_value for (key, value) in dict.items() if test_condition}

import random
names = ["Alex", "Beth", "Carol", "Dennis", "Eleven", "Fredy"]
students_score = {student: random.randint(1,100) for student in names}

passed_students = {student: score for (student, score) in students_score.items() if score > 60}
# print(passed_students)

# how to iterate over a pandas DataFrame
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 89]
}

# looping through Dictionary
# for (key, values) in student_dict.items():
#     print(key)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# looping through data frame
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# looping through rows of the data frame
# Syntax:
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

for(index, row) in student_data_frame.iterrows():
    # print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)