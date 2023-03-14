'''
Sort the odd

You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the
even numbers at their original positions.
Examples

[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
'''

def sort_array(source_array):
    for i in range(0, len(source_array)):
        for j in range(i, len(source_array)):
            if(source_array[i] % 2 == 1 and source_array[j] % 2 == 1):
                if(source_array[j] < source_array[i]):
                    num = source_array[i]
                    source_array[i] = source_array[j]
                    source_array[j] = num
    return source_array