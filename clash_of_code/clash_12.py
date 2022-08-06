import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# find the missing leg of the right angle triangle

x, h = [int(i) for i in input().split()]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

d = math.sqrt((x*x)+(h*h))

print(int(math.floor(d)))
