'''
Automorphic Number (Special Numbers Series #6)

A number is called Automorphic number if and only if its square ends in the same digits as the number itself.

Given a number determine if it Automorphic or not .
'''

def automorphic(n):
    return "Automorphic" if str((n ** 2)).endswith(str(n)) else "Not!!"

