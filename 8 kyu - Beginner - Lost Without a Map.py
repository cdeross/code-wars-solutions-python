'''
Beginner - Lost Without a Map

Given an array of integers, return a new array with each value doubled.
For example:
[1, 2, 3] --> [2, 4, 6]
'''

def maps(a):
    arr = []
    i = 0
    while i < len(a):
        arr.append(a[i]*2)
        i += 1
    return arr