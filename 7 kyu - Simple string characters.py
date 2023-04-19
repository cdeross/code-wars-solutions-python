'''
Simple string characters

In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of
uppercase letters, lowercase, numbers and special characters, as follows.

Solve("*'&ABCDabcde12345") = [4,5,5,3].
--the order is: uppercase letters, lowercase, numbers and special characters.
'''

def solve(s):
    upper = 0
    lower = 0
    number = 0
    special = 0
    for i in s:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isdigit():
            number += 1
        else:
            special += 1
    return [upper, lower, number, special]