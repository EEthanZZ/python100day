travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# TODO: Write the function that will allow new countries
# to be added to the travel_log.


def add_new_country(country, times, cities):
    for i in range(0, len(travel_log)+1):
        travel_log[-1]['country'] = country
        travel_log[-1]['visits'] = times
        travel_log[-1]['cities'] = cities


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


def add_new_country2(country, times, cities):
    new_country = {}
    new_country['country'] = country
    new_country['visits'] = times
    new_country['cities'] = cities
    travel_log.append(new_country)


add_new_country2("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
