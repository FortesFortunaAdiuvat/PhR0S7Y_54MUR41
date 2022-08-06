#Distance from rocket to mars, will it arrive in time

dist, t, s, v = [int(i) for i in input().split()]
d=0
while t>0:
    d+=s
    t-=1
    s+=v
if dist<=d:
    print("true",d)
else:
    print("false",d)