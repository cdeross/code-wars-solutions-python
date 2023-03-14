'''
Break camelCase

Complete the solution so that the function will break up camel casing, using a space between words.
Example

"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
'''

def solution(s):
    i = 0
    sen = ""
    while i < len(s):
        if s[i].islower() == True:
            sen = sen + s[i]
            i += 1
        else:
            sen = sen + " " + s[i]
            i += 1
    return sen