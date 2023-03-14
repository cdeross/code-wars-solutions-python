'''
Sum of odd numbers

Given the triangle of consecutive odd numbers:
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)
1 -->  1
2 --> 3 + 5 = 8
'''

def row_sum_odd_numbers(n):
    first_digit = (n**2 - (n-1))
    row = []
    row.append(first_digit)
    next_digit = 0
    sum = 0
    i = 0
    while i < (n -1):
        next_digit = (row[i] + 2)
        row.append(next_digit)
        i = i + 1
    for num in row:
        sum = sum + num
    return sum