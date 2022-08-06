import sys
import math

"""
Given is a greyscale image Im of width W and height H. Pixels are integers ranging from 0 to 255.
(x,y)=(0,0) addresses the top-left corner.

The integral image IntIm of Im is a 2d-array of size WxH where each value IntIm(x,y) is calculated as a sum of pixels of Im.

The pixel value of IntIm at any coordinate (x',y') is defined as the sum over all pixel values of Im(x,y) for x=0..x', y=0..y'.

So in an integral image, each pixel value is the summation over all pixels of the rectangle area between (0,0) and the pixel's coordinate.

Sample Image Im: WxH=6x4
4 2 3 5 2 7
3 7 6 9 3 8
1 1 0 6 1 2
1 4 3 2 7 1

Integral Image:
IntIm[0,0] = Im[0,0] = 4
IntIm[1,0] = Im[0,0] + Im[1,0] = 4 + 2 = 6
IntIm[2,0] = Im[0,0] + Im[1,0] + Im[2,0] = 4 + 2 + 3 = 9
...
IntIm[0,1] = Im[0,0] + Im[0,1] = 4 + 3 = 7
IntIm[0,2] = Im[0,0] + Im[0,1] + Im[0,2] = 4 + 3 + 1 = 8
...
IntIm[1,1] = Im[0,0] + Im[1,0] + Im[0,1] + Im[1,1] = 4 + 2 + 3 + 7 = 16
...
IntIm[3,2] is the sum of all the boldly marked pixels below

4 2 3 5 2 7
3 7 6 9 3 8
1 1 0 6 1 2
1 4 3 2 7 1

IntIm[3,2] = 4+2+3+5 + 3+7+6+9 + 1+1+0+6 = 47

Proceed as shown above for the remaining pixels to obtain the entire integral image ImInt:

4 6 9 14 16 23
7 16 25 39 44 59
8 18 27 47 53 70
9 23 35 57 70 88
Input
Line 1: width W as integer
Line 2: height H as integer
Next H lines: W space separated pixel values for each row of Im
Output
H lines: space separated integers of IntIm
Constraints
1 ≤ W ≤ 100
1 ≤ H ≤ 100
0 ≤ pixel of Im ≤ 255 as integer
Example
Input
6
4
4 2 3 5 2 7
3 7 6 9 3 8
1 1 0 6 1 2
1 4 3 2 7 1
Output
4 6 9 14 16 23
7 16 25 39 44 59
8 18 27 47 53 70
9 23 35 57 70 88
"""


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w,h,x=int(input()),int(input()),[]
a=[[0]*w for _ in range(h)]
x=[list(map(int,input().split())) for i in range(h)]
for j in range(h):
 for i in range(w):
  for y in range(j+1):
   for l in range(i+1):a[j][i]+=x[y][l]
for r in a:print(*r)