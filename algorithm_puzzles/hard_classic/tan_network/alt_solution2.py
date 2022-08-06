import sys
import math
from collections import namedtuple, defaultdict

Stop = namedtuple('Stop', ['id', 'name', 'lat', 'lon', 'type'])


def dist(stop1, stop2):
    lonB, latB = stop2.lon / 180 * math.pi, stop2.lat / 180 * math.pi
    lonA, latA = stop1.lon / 180 * math.pi, stop1.lat / 180 * math.pi
    x = (lonB - lonA) * math.cos((latA + latB)/2)
    y = latB - latA
    d = (x**2 + y**2)**(1/2) * 6371
    return d


def dijkstra(graph, start_node, target_node):
    unvisited_nodes = list(graph.keys())
    shortest_path = {} #cost for visiting each nodes
    previous_nodes = {} #shortest path to a node
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0

    while unvisited_nodes:
        current_min_node = None
        #let's find the node with lowest score... comprends pas !
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        #let's retrieve current node's neighbours
        if graph[current_min_node]:
            neighbours = list(graph[current_min_node].keys())
            for neighbour in neighbours:
                tentative_value = shortest_path[current_min_node] + graph[current_min_node][neighbour]
                if tentative_value < shortest_path[neighbour]:
                    shortest_path[neighbour] = tentative_value
                    previous_nodes[neighbour] = current_min_node
        #let's remove the visited node
        unvisited_nodes.remove(current_min_node)
    #let's find the path to the target_node
    
    path = []
    node = target_node
    while node != start_node:
        path.append(node)
        try:
            node = previous_nodes[node]
        except KeyError:
            return None
    path.append(start_node)
    return path[::-1]


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

graph = {} #les liaisons
stops = {} #dictionnaire des arrêts avec stop._id: Stop()
start_point = input()[9::]
end_point = input()[9::]
n = int(input())
for i in range(n):
    stop_name = input()
    _id, _name, _, lat, lon, _, _, _type, _ = stop_name.split(',')
    _id = _id[9::]
    _name = _name[1:-1:]
    lat, lon = float(lat), float(lon)
    stop = Stop(_id, _name, lat, lon, _type)
    stops[stop.id] = stop
for key, value in stops.items():
    graph[key] = {}
m = int(input())
for i in range(m):
    start, stop = input().split()
    start, stop = start[9::], stop[9::]
    graph[start][stop] = dist(stops[start], stops[stop])


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

path = dijkstra(graph, start_point, end_point)
if path:
    print('\n'.join([stops[g].name for g in path]))
else:
    print('IMPOSSIBLE')