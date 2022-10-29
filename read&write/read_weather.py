# weather_list = list()
# with open("weather_data.csv") as weather:
#     weather_day = weather.readlines()
#     print(weather_day)
#     for i in weather_day:
#         i.strip("\n")
#         print(i)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     tem = []
#     for row in data:
#         if row[1] != 'temp':
#             x = int(row[1])
#             tem.append(x)
#     print(tem)

import pandas
data = pandas.read_csv("weather_data.csv")
# print(data["day"])
data_dict = data.to_dict()
temp_list = data["temp"].to_list()
ave = sum(temp_list) / len(temp_list)
# print(ave)
# print(data["temp"].max())
# print(data.day)
# print(data["day"])

monday = data[data.day == 'Monday']
print(int(monday.temp) * 3)

data_score = {
    "student": ["Amy", "John", "Jason"],
    "scores": [10, 20, 30]
}
score = pandas.DataFrame(data_score)
print(score)