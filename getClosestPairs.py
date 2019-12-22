import csv
import math
import sys

cities = {}
cities_matrix = {}
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

for firstCity in cities.keys():
    for secondCity in cities.keys():
        d = getDistance(firstCity, secondCity)
        if d :
            cities_matrix[firstCity + ',' + secondCity] = d

winners = sorted(cities_matrix, key=cities_matrix.__getitem__)

if n:
    print(winners[0:int(n)*2:2])
else:
    print(winners)
print(n)
