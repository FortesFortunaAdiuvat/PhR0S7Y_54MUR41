# place checkbox next to odd numbers

count = int(input())
for i in input().split():
    n = int(i)
    print(f'[{["x"," "][n%2==0]}] {n}')

count = int(input())
for i in input().split():
    n = int(i)
    if n % 2 != 0:
        print('[x] '+i)
    elif n % 2 == 0:
        print('[ ] '+i)
