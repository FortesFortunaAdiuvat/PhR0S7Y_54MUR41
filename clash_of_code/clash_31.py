# Ceasar Box
# https://www.wikihow.com/Decode-a-Caesar-Box-Code
# convert string to grid with equal rows and columns
# read grid top to bottom, left to right to decode

import math
m=input();v = len(m);l=[];a,k=0,int(math.sqrt(v));b=k
for i in range(k):l.append(m[a:b]);a=b;b+=k
lis=[[l[i][j]for i in range(k)]for j in range(k)]
for i in lis:print(*i,sep='',end='')
