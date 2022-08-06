import sys
import math
import logging
from collections import defaultdict, namedtuple

logging.basicConfig(level=logging.DEBUG)

Station = namedtuple('Station', ['id', 'title', 'lat', 'long'])

def parse_id(s: str):
    prefix = 'StopArea:'
    assert s.startswith(prefix)
    assert ',' not in s
    return s[len(prefix):]


def parse_station(s: str):
    prefix = 'StopArea:'
    assert s.startswith(prefix)
    el = s[len(prefix):].split(',')    
    return Station(el[0], el[1][1:-1], float(el[3]), float(el[4]))


def distance(a: Station, b: Station):
    x = (b.long - a.long) * math.cos((a.lat + b.lat) / 2)
    y = b.lat - a.lat
    return math.hypot(x, y) * 6371
        

start_point = parse_id(input())
end_point = parse_id(input())

nodes = {}
for i in range(int(input())):
    station = parse_station(input())
    nodes[station.id] = station

links = defaultdict(list)
rlinks = defaultdict(list)
for i in range(int(input())):
    start, end = map(parse_id, input().split(' '))
    links[start].append(end)
    rlinks[end].append(start)


def bfs_r(start, end):
    que = [end]
    lengths = {end: 0}
    while que:
        logging.debug(lengths)
        node, que = que[0], que[1:]
        
        #if node == start:
        #    break
        
        for neighbor in rlinks[node]:
            length = lengths[node] + distance(nodes[node], nodes[neighbor])
            if neighbor in lengths:
                lengths[neighbor] = min(length, lengths[neighbor])
            else:
                lengths[neighbor] = length
                que.append(neighbor)
        que.sort(key=lambda p: lengths[p])
                
    if start not in lengths:
        return None
        
    path = []
    while start != end:
        path.append(start)
        start = min(links[start], key=lambda p: lengths[p])
    return path + [end]
            

best_path = bfs_r(start_point, end_point)
print('\n'.join(nodes[p].title for p in best_path) if best_path else 'IMPOSSIBLE')