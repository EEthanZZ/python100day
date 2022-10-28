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
print(data)
