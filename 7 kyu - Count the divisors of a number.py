'''
Count the divisors of a number


Random tests go up to n = 500000.
Examples (input --> output)

4 --> 3 (1, 2, 4)
5 --> 2 (1, 5)
12 --> 6 (1, 2, 3, 4, 6, 12)
30 --> 8 (1, 2, 3, 5, 6, 10, 15, 30)
Note you should only return a number, the count of divisors. The numbers between parentheses are shown only for you to
see which numbers are counted in each case.
'''

def divisors(n):
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
            i += 1
        else:
            i += 1
    return count