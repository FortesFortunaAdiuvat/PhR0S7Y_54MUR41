import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s0 = int(input())
n = int(input())
mul, inc = [int(i) for i in input().split()]

a = [s0]

for i in range(1, n + 1):
    if i % 2:
        a += [a[i-1] * mul + inc]
    else:
        a += [a[i-1] * mul - inc]

print(a[-1])