# remove a biscuit shape from dough given height and width of dough, (x,y) of center of biscuit and diameter d of biscuit

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

h, w, x, y, d = [int(i) for i in input().split()]

for i in range(h):
    r=''
    for j in range(w):
        r+='  ' if math.dist([x,y],[j,i]) <= d/2 else '{}'
    print(r)
    