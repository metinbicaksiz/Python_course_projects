# with open("weather_data.csv") as file:
#     words = file.readlines()
#     print(words)
#
# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#

import pandas
# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# list = data["temp"].to_list()

# print(data["temp"].mean()) # mean
# print(data["temp"].max()) # max
# print(data["temp"].min()) # min
# print(data["temp"].sum()) # sum

# print(data.temp.max())

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# print(monday_temp * 9/5 + 32)

# Create a DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

dataFr = pandas.DataFrame(data_dict)
dataFr.to_csv("new_data.csv")