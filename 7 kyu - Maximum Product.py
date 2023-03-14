'''
Maximum Product

Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array.
Notes

Array/list size is at least 2.
Array/list numbers could be a mixture of positives, negatives also zeroes .
'''

def adjacent_element_product(array):
    largest = -10000000000000000000000
    cur_sum = 0
    for i in range(len(array)-1):
        cur_sum = array[i] * array[i+1]
        if cur_sum > largest:
            largest = cur_sum
    return largest