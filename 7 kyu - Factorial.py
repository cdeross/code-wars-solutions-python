'''
Factorial

Your task is to write function factorial.
'''

def factorial(n):
    total = 1
    for i in range(n+1):
        if i == 0:
            pass
        else:
            total *= i
    return total