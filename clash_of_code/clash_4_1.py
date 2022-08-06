import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
def is_vowel(c):
    return c in 'aeiou'

ttl = 0
for i in range(1, len(s), 2):
    if is_vowel(s[i].lower()):
        ttl += 1
print(ttl)
print(s, file=sys.stderr, flush=True)