import sys
import math

'''
Create a rectangle based on the specified height and width parameters. Use the letter "O" (Case-Sensitive) as the character making up the rectangle.
'''


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

height = int(input())
width = int(input())

answer = ''


for j in range(0, width):
    answer += 'O'

for i in range(0, height):
    print(answer)
    

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

