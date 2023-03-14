'''
Is it a palindrome?

Write a function that checks if a given string (case insensitive) is a palindrome.
'''

def is_palindrome(s):
    return True if s.lower() == s[::-1].lower() else False