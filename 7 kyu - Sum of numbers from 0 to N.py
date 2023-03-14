'''
Sum of numbers from 0 to N

We want to generate a function that computes the series starting from 0 and ending until the given number.
Example:

Input:
> 6
Output:
0+1+2+3+4+5+6 = 21
Input:
> -15
Output:
-15<0
Input:
> 0
Output:
0=0
'''

def show_sequence(n):
    total = 0
    strng = ""
    if n == 0:
        return "0=0"
    if n < 0:
        return "{}<0".format(n)
    else:
        for i in range(n+1):
            total += i
            strng = strng + str(i) + "+"
        return strng[:-1] + " = " + str(total)