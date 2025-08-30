# with open("../../data/weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("../../data/weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("../../data/weather_data.csv")
# print(data["temp"])

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)

# avg = sum(temp_list)/len(temp_list)
# print(avg)

# print(data["temp"].mean())

# print(data["temp"].max())

# Get data in column
# print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])

# Get data in row with maximum temperature
# print(data[data.temp == data["temp"].max()])

# Get particular data if condition match
monday = data[data.day == "Monday"]
# print(monday["temp"])
# print((monday["temp"] * 1.8) + 32)

# Create Dataframe from scratch
data_dict = {
    "students": ["Punam", "Sudipa", "Sujit"],
    "gpa": [3.4, 3.8, 3.7]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("../../data/gpa.csv")