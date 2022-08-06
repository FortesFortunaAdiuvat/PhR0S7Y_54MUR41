import sys
import math

stops, routes = {}, {}
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

start_point = input()
end_point = input()
n = int(input())
for i in range(n):
    stop_name = input().split(",")
    stop_name[1] = stop_name[1][1:-1]
    stop_name[3] = float(stop_name[3]) * math.pi / 180
    stop_name[4] = float(stop_name[4]) * math.pi / 180
    stops[stop_name[0]] = [stop_name[1], stop_name[3], stop_name[4]]
m = int(input())
for i in range(m):
    route0, route1 = input().split()
    if route0 != route1:
        if route0 not in routes:
            routes[route0] = [route1]
        else:
            routes[route0].append(route1)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
answer = "IMPOSSIBLE"
if start_point in routes:
    if start_point == end_point:
        answer = stops[end_point][0]
    elif end_point in routes[start_point]:
        answer = stops[start_point][0] + "\n" + stops[end_point][0]
    else:
        visitedNodes = {}
        queue = [start_point]
        visitedNodes[start_point] = [0, ""]
        found = False
        while queue != []:
            thisNode = queue.pop(0)
            if thisNode == end_point:
                found = True
                break
            distsofar = visitedNodes[thisNode][0]
            x0, y0 = stops[thisNode][1], stops[thisNode][2]
            neighbours = routes[thisNode]
            for neighbour in neighbours:
                x1, y1 = stops[neighbour][1], stops[neighbour][2]
                x = (y1 - y0) * math.cos((x0 + x1) / 2)
                y = x1 - x0
                dist = ((x ** 2 + y ** 2) ** 0.5) * 6371
                distfurther = distsofar + dist
                if neighbour not in visitedNodes:
                    queue.append(neighbour)
                    visitedNodes[neighbour] = [distfurther, thisNode]
                elif distfurther < visitedNodes[neighbour][0]:
                    visitedNodes[neighbour] = [distfurther, thisNode]
            queue.sort(key = lambda x: visitedNodes[x][0])
        if found:
            answer, i = stops[end_point][0], end_point
            while i != start_point:
                j = visitedNodes[i][1]
                answer = stops[j][0] + "\n" + answer
                i = j

print(answer)