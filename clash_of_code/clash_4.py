import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

'''
Almost all of the words contain vowels. The letters which are considered to be vowels (in English) are a,e,i,o,u.
Display the total number of vowels present at odd indexes in the given string.
'''

vowels = ['a', 'e', 'i', 'o', 'u']

vowel_count = 0

s = input()
odd_string = s[1::2].lower()

for i in odd_string:
    for j in vowels:
        if j == i:
            vowel_count +=1





# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(vowel_count)
