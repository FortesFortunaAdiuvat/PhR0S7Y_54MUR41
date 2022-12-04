#highest power of 2 that divices a given number

def highestPowerOf2(n):
 
    return (n & (~(n - 1)))
 
def alternate(n):
    return max(2**i for i in range(ceil(log2(n))+1)if n%2**i==0)


n = int(input())
print(highestPowerOf2(n))
