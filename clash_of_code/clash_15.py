import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#Grasshoper loses health e and gains health a every day(iteration), output health of grasshoper or Dead if 0


d = int(input())
g, e, a = [int(i) for i in input().split()]

for i in range(d):
    g = g - e + a

print(g if g > 0 else "Dead")
