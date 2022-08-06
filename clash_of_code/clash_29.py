'''
You should calculate the value of material on the chessboard for both sides black and white. Relying on that deep and solid analysis, output who is better.

White pieces represented as uppercase letters, black pieces as lowercase letters (P/p for pawns, N/n for knights, B/b for bishops, R/r for rooks, Q/q for queens, K/k for kings). Blank squares shown as spaces and dots.

~ Pawn cost 1 point.
~ kNight or Bishop cost 3 points.
~ Rook cost 5 points.
~ Queen cost 9 points.
~ King cost nothing.
Input
Next 8 lines: Collection of strings describing position on the board. Each line reveals eight squares in a row.
Output
Single line: message "white is better", "black is better" or "equal", overall value of material for white and value for black, all separated by spaces.
Constraints
Example
Input
 . . . .
p . . . 
 . . . .
. . . . 
 . . . .
. . . . 
 . . . .
. . . . 
Output
black is better 0 1
'''

w=0
b=0
p = {'p':1,'n':3,'b':3,'r':5, 'q':9, 'k':0}
for i in range(8):
    l = input()
    for j in l:
        if j.isupper() and j.lower() in p:
            w+=p[j.lower()]
        elif j.islower() and j.lower() in p:
            b+=p[j.lower()]

if b > w:
    print(f'black is better {w} {b}')
elif w > b:
    print(f'white is better {w} {b}')
elif w == b:
    print(f'equal {w} {b}')
        

########
b=0
w=0
for i in'_'*8:
 l=input()
 for k,v in{'p':1,'n':3,'b':3,'r':5,'q':9}.items():
  b+=l.count(k)*v
  w+=l.count(k.upper())*v
if b==w:print('equal',b,w);_
print(['white','black'][w<b],'is better',w,b)
#####
d={'p':1,'n':3,'b':3,'r':5,'q':9,'k':0}
w,b=0,0
for i in range(8):
 for c in input():
  if c.isupper():
   w+=d[c.lower()]
  elif c.islower():
   b+=d[c]
print("equal"if w==b else("black"if b>w else"white")+" is better",w,b)