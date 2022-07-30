import sys
import math


n = int(input())  # the number of temperatures to analyse
temperatures = input().split()

closest_to_zero_temperature = 0

if n != 0:
    closest_to_zero_temperature = int(temperatures[0])
    for i in temperatures:
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = abs(int(i))
        if t < abs(closest_to_zero_temperature):
            closest_to_zero_temperature = int(i)
        elif (t == abs(closest_to_zero_temperature)) and (int(i) > 0 ):
            closest_to_zero_temperature = t
    
print(closest_to_zero_temperature)
