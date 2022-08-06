# sum unary numbers, output sum in unary

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.



count = int(input())
complete_total = 0
for unary in input().split():
    total = 0
    for i in unary:
        total += 1

    complete_total += total

unary_string = ''
for i in range(complete_total):
    unary_string += '1'

print(unary_string)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

