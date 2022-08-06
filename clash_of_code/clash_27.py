# extract upper case characters from encoded message, lower case them, and print the decrypted message

t = input()
for i in t:
    if(i.isupper()):
        print(i.lower(),end="")

#####
t = input()
w = ''
for i in t:
    if i.isupper():
        w += i
print(w.lower())

#####
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

text = input()
message_text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = ''
for char in text:
    if char in message_text:
        message+=char

print(message.lower())