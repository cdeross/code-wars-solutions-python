'''
Maximum subarray sum

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list
of integers:
max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
If the list is made up of only negative numbers, return 0 instead.
Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
'''

def max_sequence(arr):
    cur_sum = 0
    max = 0
    for i in arr:
        tmp_sum = i
        if cur_sum + tmp_sum > 0:
            cur_sum = cur_sum + tmp_sum
            if cur_sum > max:
                max = cur_sum
        else:
            cur_sum = 0
    return max