import sys
import math

text = input()
lt = len(text)
for i in range(1,lt):
    p = text[:i]
    n = math.ceil(lt/len(p))
    pn = (p*n)[:lt]
    if pn == text:
        if n==lt/len(p):
            print(f'{p}*{n}')
        else:
            part = lt-len(p)*(n-1)
            print(f'{p}*({n-1}+{part}/{len(p)})')
        break
else:
    print(text,'*',1,sep='')

