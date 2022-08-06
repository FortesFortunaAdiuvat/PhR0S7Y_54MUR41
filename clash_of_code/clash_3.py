import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

'''
You are given a string made of a word repeated several time, followed by a part of that same word.

You have to find that word, the number of times it is repeated, and the size of the final part. Then, output the whole as a string formatted like this:
the_word*(number_of_repetition+part_size/word_size)

If the final part is empty, output only the word and the number, as a string formatted like this:
the_word*number_of_repetition

You have to find the smallest word possible. For example, "hahahahahahah" could be written as "haha*(3+1/4)" and also as "ha*(6+1/2)". The good answer is the second formatting, where the repeated word is smaller.

The given string contains only alphabetic lower-case characters, so you don't have to care about case-sensitiveness.

Input
text: a string.
Output
A string, formatted as "w*(n+p_s/w_s)" or as "w*n".
'''

text = input()

def repeats(string):
    for x in range(1, len(string)):
        substring = string[:x]

        if substring * (len(string)//len(substring))+(substring[:len(string)%len(substring)]) == string:
            print(substring)
            return "break"

    return(string)

the_word = repeats(text)
word_size= len(the_word)
part_size = len(text) - word_size

repetitions = text.count(the_word)
    


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)



print(the_word+str())