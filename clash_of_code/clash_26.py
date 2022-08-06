# Find perfect or flawed powers of a number such that a^r=n. Example 3^3 = 9 is Perfect

f=lambda:bin(int(input()))[2:].zfill(24)
a=f()
b=f()
c=lambda i,j:min(255,int(a[i:j],2)+int(b[i:j],2))
print(c(0,8),c(8,16),c(16,24))
