import sys
import math
from collections import defaultdict
from queue import PriorityQueue


class Stop():
    def __init__(self, id, name, lat, lon, t):
        self.id = id
        self.name = name
        self.lon = float(lon)
        self.lat = float(lat)
        self.type = t
    
    def __str__(self):
        return self.name


def distance(a, b):
    R = 6371
    x = (b.lon - a.lon) * math.cos(((a.lat + b.lat) * math.pi/180 ) / 2)
    y = b.lat - a.lat
    d = math.sqrt(x * x + y * y) * R
    return d


def shortest_route(start, end):
    global STOPS
    global ROUTES

    q = PriorityQueue()
    dist = defaultdict(lambda: float('inf'))
    prev = defaultdict(str)

    dist[start] = 0
    q.put((dist[start], start))

    while not q.empty():
        node = q.get()[1]

        if node == end:
            route = []
            while node != start:
                route.append(node)
                node = prev[node]
            route.append(start)
            return route[::-1]

        for stop in ROUTES[node]:
            alt = dist[node] + distance(STOPS[node], STOPS[stop])
            if alt < dist[stop]:
                dist[stop] = alt
                prev[stop] = node
                if stop not in [item[1] for item in q.queue]:
                    q.put((alt, stop))

    print('IMPOSSIBLE')
    return


STOPS = defaultdict(object)
ROUTES = defaultdict(list)

start_point = input().replace('StopArea:', '')
end_point = input().replace('StopArea:', '')

n = int(input())
for i in range(n):
    data = input().replace('StopArea:', '').split(',')
    stop = Stop(data[0], data[1].replace("\"", ''), data[3], data[4], data[7])
    STOPS[data[0]] = stop

m = int(input())
for i in range(m):
    data = input().replace('StopArea:', '').split()
    ROUTES[data[0]].append(data[1])

if start_point == end_point:
    print(STOPS[start_point])

elif end_point in ROUTES[start_point]:
    print(STOPS[start_point])
    print(STOPS[end_point])

else:
    route = shortest_route(start_point, end_point)
    if route:
        for stop in route:
            print(STOPS[stop].name)
