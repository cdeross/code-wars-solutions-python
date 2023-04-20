'''
Alternate case

Write function alternateCase which switch every letter in string from upper to lower and from lower to upper.
E.g: Hello World -> hELLO wORLD
'''

def alternate_case(s):
    sen = ""
    for i in s:
        if i.isupper():
            sen += i.lower()
        elif i.islower():
            sen += i.upper()
        else:
            sen += i
    return sen