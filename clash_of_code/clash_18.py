import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

'''
You are given a number N and a list of integers. You must output exactly 2 numbers that are in the list and their sum is equal to N
Input
Line 1: An integer N for the target sum.
Line 2 : An integer L for the length of the list.
Line 3 : A list of space separated integers to look for the target number.
Output
A single line of exactly 2 space separated integers that sum up to N if such exist in the array, N/A otherwise. Smaller number first.
Constraints
-100 <= N <= 100
2 <= array length <= 10
-100 <= array elements <= 100
'''

n = int(input())
l = int(input())
flag = False

for i in input().split():
    x = int(i)
    for y in range(l):
        if y + x == n:
            if y > x:
                print(f'{x} {y}')
                
            else:
                print(f'{y} {x}')
                flag = True

if flag == False:
    print('N/A')
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

#####################
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a1 = []
a2 = 0
n = int(input())
l = int(input())
for i in input().split():
    x = int(i)
    a1.append(x)
    for e in a1:
        y = int(e)
        if x+y == n:
            if x < y:
                print(x,y)
            else:
                print(y,x)
            exit()

print("N/A")


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
###############
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
found = False
n = int(input())
l = int(input())
matrix = []
for i in input().split():
    x = int(i)
    matrix.append(x)

for i in matrix:
    for j in matrix:
        if i + j == n:
            print(min(i, j), max(i, j))
            found = True
            break
    if found == True:
        break

if not found:
    print("N/A")


