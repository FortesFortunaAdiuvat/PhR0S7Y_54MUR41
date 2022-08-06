import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#Sum the diaganols of a matrix

t = 0
n = int(input())
if n < 2:
    print(input())
    exit()
for i in range(n):
    b = input()
    # print(b)
    a = list(map(int, b.split()))
    t += a[i] + a[n-i-1]
    if i == n-i-1:
        t -= a[i]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(t)