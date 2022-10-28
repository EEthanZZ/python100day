# weather_list = list()
# with open("weather_data.csv") as weather:
#     weather_day = weather.readlines()
#     print(weather_day)
#     for i in weather_day:
#         i.strip("\n")
#         print(i)

import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)