'''
Shortest Word

Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.
'''

def find_short(s):
    arr = s.split()
    length = 10000
    for i in arr:
        if length > len(i):
            length = len(i)
        else:
            pass
    return length