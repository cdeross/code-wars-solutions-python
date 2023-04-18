'''
Divide and Conquer

Given a mixed array of number and string representations of integers, add up the non-string integers and subtract the
total of the string integers.
Return as a number.
'''

def div_con(x):
    alpha = 0
    num = 0
    for i in x:
        if type(i) == str:
            alpha = alpha + int(i)
        else:
            num = num + i
    return num - alpha