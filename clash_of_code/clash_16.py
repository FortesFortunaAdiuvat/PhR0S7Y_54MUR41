import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# decrement every int in a string and remove zero's

n = int(input())

new_string = ''
for i in str(n):
    if i != "0":
        i = int(i)-1
        new_string+=str(i)
    else:
        new_string+=str("")

print(new_string)
