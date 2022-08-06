# inputs are 'guitar' and 'drums', guitar alternates between plinx and plonx, drums output badum, unless the final iteration/note then they play 'tss'

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
guitar_switch = False
for i in range(n):
    instrument = input()
    if instrument == 'guitar' and guitar_switch == False:
        print('plinx')
        guitar_switch = True
    elif instrument == 'guitar' and guitar_switch == True:
        print('plonx')
        guitar_switch=False
    elif instrument == 'drums' and i != n-1:
        print('badum')
    elif instrument == 'drums' and i == n-1:
        print('tss')
    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

##############
n = int(input())
instruments = []
for i in range(n):
    instruments.append(input())

last_guitar = "plonx"
for i, inst in enumerate(instruments):
    if inst == "guitar":
        last_guitar = "plinx" if last_guitar == "plonx" else "plonx"
        print(last_guitar)
    else:
        print("badum" if i != len(instruments) - 1 else "tss")

