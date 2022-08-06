import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# Given and int n, sum the even numbers in range starting 2 to n (inclusive) and output the sum

n = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
evens_list = []
for i in range(2, n+1):
    if i % 2 == 0:
        evens_list.append(int(i))

k = sum(evens_list)

print(k)


# alternate solution
ans=0

for x in range(2,n+1):
    if x % 2 == 0:
        ans+=x

print(ans)
