import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#reverse test case clash - output string with product, summation, and subtraction of two vars

a, b = [int(i) for i in input().split()]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

answer1 = a*b
answer2 = a+b
answer3 = a-b

answer = str(answer1)+str(answer2)+str(answer3)
#print(f"{a*b}{a+b}{a-b}")
print(answer)
