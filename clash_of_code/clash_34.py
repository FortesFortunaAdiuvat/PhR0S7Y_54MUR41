import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#Reverse Challenge - print a semaphore box
# A full row at the top
# Spaces in between first and last for middle rows
# A centered # in the center at the last line
#
"""
#####
#   #
#   #
#   #
# # #
"""


h = int(input())
w = int(input())

print(w*"#")
for i in range(h-2):
    print("#"+" "*(w-2)+"#")
print("#"+(w//2-1)*" "+"#"+(w//2-1)*" "+"#")


############

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

h = int(input())
w = int(input())

print('#'*w)
for i in range(h-2):
    print('#'+' '*(w-2)+'#')
print('#'+'#'.center(w-2)+'#')