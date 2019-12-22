import csv
import math
import sys

cities = {}
cities_matrix = {}
capital_to_country = {}
R = 6371 # Radius of the Earth in Km
n = None
try:
    n = sys.argv[1]
except IndexError:
    pass

def getDistance(city1, city2):
    if 'city1' != 'city2':
        lat1, long1 = cities[city1]
        lat2, long2 = cities[city2]
        dLat = (lat2 - lat1) * math.pi/180
        dLon = (long2 - long1) * math.pi/180
        a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(lat1 * math.pi/180) * math.cos(lat2 * math.pi/180) * math.sin(dLon/2) * math.sin(dLon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a));
        return R * c
    else:
        print("Invalid query: these are the same cities")

with open('country-capitals.csv', 'r') as f:
    citiesReader = csv.reader(f)
    for line in citiesReader:
        if line[0] != 'CountryName':
            if line[2] != ' D.C.':
                cities[line[1]] = (float(line[2]), float(line[3]))
            if line[2] == ' D.C':
                cities[line[1]] = (float(line[3]), float(line[4]))
        capital_to_country[line[1]] = line[0]

for firstCity in cities.keys():
    for secondCity in cities.keys():
        d = getDistance(firstCity, secondCity)
        if d :
            key = firstCity + ', ' + capital_to_country[firstCity] + ' : ' +secondCity + ', ' + capital_to_country[secondCity]
            cities_matrix[key] = d

winners = sorted(cities_matrix, key=cities_matrix.__getitem__)

i = 1
if n:
    for winner in winners[0:int(n)*2:2]:
        print(str(i) + ". " + winner + " (%.2f km)" % cities_matrix[winner])
        i += 1
else:
    for winner in winners[::2]:
        print(str(i) + ". " + winner + " (%.2f km)" % cities_matrix[winner])
        i += 1
