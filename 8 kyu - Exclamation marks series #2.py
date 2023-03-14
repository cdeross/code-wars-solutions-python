'''
Exclamation marks series #2

Remove all exclamation marks from the end of sentence.
Examples

remove("Hi!") === "Hi"
remove("Hi!!!") === "Hi"
remove("!Hi") === "!Hi"
remove("!Hi!") === "!Hi"
remove("Hi! Hi!") === "Hi! Hi"
remove("Hi") === "Hi"
'''

def remove(s):
    strng = s
    i = 1
    while s[-i] == "!":
        strng = strng[:-1]
        i += 1
        print(strng)
    return strng