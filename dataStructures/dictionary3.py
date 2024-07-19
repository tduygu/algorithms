import random

city_names = ['Paris', 'London', 'Rome', 'Berlin', 'Madrid', 'Ankara']
city_temperatures = {city: random.randint(20,35) for city in city_names}
print(city_temperatures)

hot_cities = {"hot_"+key: value for (key, value) in city_temperatures.items() if value>30}
print(hot_cities)

