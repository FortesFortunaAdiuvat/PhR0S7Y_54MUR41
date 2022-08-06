'''
You get an 'encrypted' string as your input (X). You have to create a new string as follows:
- pick the leftmost character from X
- pick the rightmost character from X
- pick the second leftmost character from X
- pick the second rightmost character from X
- ... continue until you have used all the characters in X

Example:
- Input: Hlole
- Leftmost character: H
- Rightmost character: e
- Second leftmost character: l
- Second rightmost character: l
- Third leftmost character: o
- No other characters left, so your output should be: Hello
'''


x = input()
s=""
for i in range(int(len(x)/2)):
    s+=x[i]+x[len(x)-1-i]
if(len(x)&1):
    s+=x[int(len(x)/2)]
print(s)


x = input()
out=""
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
i = 0
while i < len(x):
    out += x[i]
    i+=1
    out += x[len(x)-i]
print(out[0:i])