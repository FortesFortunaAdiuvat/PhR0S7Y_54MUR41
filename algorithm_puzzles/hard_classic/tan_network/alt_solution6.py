import sys
import math

class Node():
    def __init__(self, uid):
        self.uid = uid
        self.dist = math.inf
        self.links = set()
        self.parent = None
        self.edges = dict()
        self.label = ''
        self.latitude = 0.
        self.longitude = 0.

start_point = input()
end_point = input()
n = int(input())
network = {}

for i in range(n):
    uid, label, _, lat, longi, _, _, stype, _ = input().split(',')
    node = network[uid] = Node(uid)
    node.label, node.latitude, node.longitude = eval(label), math.radians(float(lat)), math.radians(float(longi))
    

def geo_dist(A, B):
    x = (B.longitude - A.longitude) * math.cos((A.latitude + B.latitude)/2)
    y = B.latitude - A.latitude
    return 6371 * math.sqrt(x**2 + y**2)


m = int(input())
for i in range(m):
    parent, child = map(network.get, input().split())
    parent.links.add(child)


to_process = set(network.values())
start_node = network[start_point]
end_node = network[end_point]

start_node.dist = 0

while to_process:

    node = min(to_process, key=lambda x: x.dist)
    if node.dist == math.inf:
        break #Rest of the network is unreachable from start_node

    to_process.remove(node)
    for link in node.links&to_process:
        dist = node.dist + geo_dist(node, link)
        if dist < link.dist:
            link.dist = dist
            link.parent = node


path = [end_node]
while path[-1] != start_node :
    parent = path[-1].parent
    if parent is None:
        print('IMPOSSIBLE')
        break
    else:
        path += parent,
else:
    print(*map(lambda x:x.label, path[::-1]), sep='\n')


