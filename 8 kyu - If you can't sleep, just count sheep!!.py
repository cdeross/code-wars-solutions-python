'''
If you can't sleep, just count sheep!!

If you can't sleep, just count sheep!!
Task:

Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...".
Input will always be valid, i.e. no negative integers.
'''

def count_sheep(n):
    i = 0
    sentence = ''
    while i < n:
        sentence = sentence + str(i + 1) + ' sheep...'
        i = i + 1
    return sentence