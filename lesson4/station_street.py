# Объединить наборы данных из предыдущих задач и посчитать, у какой станции метро больше всего остановок 
# (в радиусе 0.5 км).

import json
import operator
from datetime import datetime
from collections import Counter
import gpxpy.geo

def get_distance(lat1, lon1, lat2, lon2):
    # расстояние между двумя точками
    return gpxpy.geo.haversine_distance(lat1, lon1, lat2, lon2)

station_data = json.load(open('data-397-2018-02-27.json', encoding="cp1251"))
street_data = json.load(open('data-398-2018-02-13.json', encoding="cp1251"))


# в файле перечислены входы, а не станции. Сделаем словарь станций с координатами station_dict
station_dict = {}
for station in station_data:
    station_lat = float(station["Latitude_WGS84"])
    station_lon = float(station["Longitude_WGS84"])
    if station['NameOfStation'] not in station_dict:
        station_dict[station['NameOfStation']] = {
        "Latitude_WGS84": float(station["Latitude_WGS84"]),
        'Longitude_WGS84': float(station["Longitude_WGS84"])
        }

# считаем количество остановок 
cnt = Counter()
for station_name, station in station_dict.items():
    station_lat = float(station["Latitude_WGS84"])
    station_lon = float(station["Longitude_WGS84"])
    for street in street_data:
        street_lat = float(street["Latitude_WGS84"])
        street_lon = float(street["Longitude_WGS84"])
        dist = get_distance(station_lat, station_lon, street_lat, street_lon)
        if dist <= 500:
            cnt[station_name] += 1

print ("Станции с наибольшим числом остановок в радиусе 500 метров:")
for station, number in cnt.most_common(20):
    print ('Рядом со станцией "{}" {} остановок'.format(station, number))
