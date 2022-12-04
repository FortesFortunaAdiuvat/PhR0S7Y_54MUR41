'''
You have to test if a sentence complies with our rule.

Our rule : a sentence is valid if by successively rotating its words to the right we can find a form of the sentence whose words' sizes make a increasing sequence of difference 1.

Example with the sentence "The grey Mo" and its two only possible rotated forms:
The grey Mo >>> Mo The grey >>> grey Mo The
It's a valid sentence because "Mo The grey" forms a sequence of words of size 2 3 4, and 2<3<4 and 3-2=1 and 4-3=1
'''

L=len
s=input().split()
for i in range(L(s)):
 if all(L(b)==L(a)+1 for a,b in zip(s,s[1:])):print(*s);exit()
 s=s[1:]+[s[0]]
print('ERROR')