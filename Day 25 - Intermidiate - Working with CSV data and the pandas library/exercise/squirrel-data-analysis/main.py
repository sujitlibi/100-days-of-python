import pandas

data = pandas.read_csv("../../data/central_park_squirrel_census_squirrel_data.csv")

fur_color = ["Gray", "Cinnamon", "Black"]
fur_color_count = []

for color in fur_color:
    # fur_color_count.append(int(data["Primary Fur Color"][data["Primary Fur Color"] == color].count())) my logic
    fur_color_count.append(len(data[data["Primary Fur Color"] == color])) # Angela Style

fur_color_count_dict = {
    "Fur Color": fur_color,
    "Count": fur_color_count
}

df = pandas.DataFrame(fur_color_count_dict)
df.to_csv("../../data/squirrel_count.csv")



