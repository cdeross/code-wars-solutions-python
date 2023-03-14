'''
Simple Fun #176: Reverse Letter

Given a string str, reverse it and omit all non-alphabetic characters.
Example

For str = "krishan", the output should be "nahsirk".
For str = "ultr53o?n", the output should be "nortlu".
Input/Output

[input] string str
A string consists of lowercase latin letters, digits and symbols.
[output] a string
'''

def reverse_letter(string):
    word = ""
    for i in string:
        if i.isalpha() == True:
            word = word + i
        else:
            pass
    return word[::-1]