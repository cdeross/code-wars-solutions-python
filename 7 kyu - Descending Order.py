'''
Descending Order

Your task is to make a function that can take any non-negative integer as an argument and return it with its digits
 in descending order. Essentially, rearrange the digits to create the highest possible number.
Examples:

Input: 42145 Output: 54421
Input: 145263 Output: 654321
Input: 123456789 Output: 987654321
'''

def descending_order(num):
    digits = []
    rev = ""
    digits = list(str(num))
    length = len(str(num))
    i = 0
    while i < int(length):
        rev = rev + max(digits)
        digits.remove(max(digits))
        i += 1
    return int(rev)