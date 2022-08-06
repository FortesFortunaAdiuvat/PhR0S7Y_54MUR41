import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(sum([1 for k,i in enumerate(s)if i.lower() in "aeiou" and k%2!=0]))