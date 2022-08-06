import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

'''
Your goal is to provide the operation table of a give operation, between all numbers in a provided range.
You receive a start and end number that indicate the range of numbers in the row headers and column headers, and an operator to perform the operations.
The operators are: + , - , and *.
Here is an example:
2 6
+

+ 2 3 4 5 6
2 4 5 6 7 8
3 5 6 7 8 9
4 6 7 8 9 10
5 7 8 9 10 11
6 8 9 10 11 12
'''


line = input()
operator = input()

start_num = line.split()[0]
end_num = line.split()[1]

for i in range(0, int(end_num)):
    

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("table")