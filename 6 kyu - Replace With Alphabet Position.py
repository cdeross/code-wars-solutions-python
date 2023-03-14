'''
Replace With Alphabet Position

In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.
Example

alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )
'''

def alphabet_position(text):
    str_num = ""
    counter = 1
    sentence = text.lower()
    sentence = "".join(i for i in sentence if i.isalpha())
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for t in sentence:
        for a in alpha:
            if t == a:
                str_num = str_num + str(counter) + " "
                counter = 1
                break
            else:
                counter += 1
    return str_num[:-1]