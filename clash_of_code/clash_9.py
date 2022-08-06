import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# Convert celsius to farenheit, and print if b is higher, lower or same then t

def cel_to_f(temp):
    return (temp*9/5)+32

n = int(input())
for i in range(n):
    b, t = [int(j) for j in input().split()]
    if b > cel_to_f(t):
        print("Higher")
    elif b < cel_to_f(t):
        print("Lower")
    else:
        print("Same")


