import sys
import math

# functions
to_float = lambda x: float(x.replace(',', '.'))

# gather inputs
lon = to_float(input())
lat = to_float(input())
n = int(input())
defibs = []

for i in range(n):
    defib_data = input().split(';')
    defibs += [{'name': defib_data[1],
               'address': defib_data[2],
               'ph': defib_data[3],
               'lon': defib_data[4],
               'lat': defib_data[5]}]

# check the distance of each defib
dists = []
for defib in defibs:
    lonb = to_float(defib['lon'])
    latb = to_float(defib['lat'])
    x = (lon - lonb)*math.cos((lat+latb)/2)
    y = lat - latb
    d = math.sqrt((x**2)+(y**2))*6371
    dists += [d]
    
# check for the closest defib
dist, closest_id = min((val, id) for (id, val) in enumerate(dists))
print(defibs[closest_id]['name'])

# This solution works fine, but for a much more golfed solution:
# from math import cos, hypot

# i=input
# r = lambda x:float(x.replace(',', '.'))
# c = 21000,''
# l, p = r(i()), r(i())
# for k in range(int(i())):
#     d = i().split(';')
#     dl, dp = r(d[4])-l, r(d[5])-p
#     c = min(c, (hypot(dl * cos(p + dp / 2), dp), d[1]))
# print(c[1])