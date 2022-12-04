n = int(input())
s = 0
r = n
for i in range(1,n+1):
    s+=i
    r-=i
    if r <0:
        r+=i
    if s > n:
        print(f'{i-1} {r}')
        break
    if s == n:
        print(f'{i} {r}')
        break
else:
    print('0 0')
    