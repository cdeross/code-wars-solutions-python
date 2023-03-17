'''
pick a set of first elements

Write a function to get the first element(s) of a sequence. Passing a parameter n (default=1) will return the first
n element(s) of the sequence.
If n == 0 return an empty sequence []
Examples

arr = ['a', 'b', 'c', 'd', 'e']
first(arr)    # --> ['a']
first(arr, 2) # --> ['a', 'b']
first(arr, 3) # --> ['a', 'b', 'c']
first(arr, 0) # --> []
'''

def first(seq, n=1):
    return [] if seq == [] else [i for i in seq[:n]]

print(first( ['a', 'b', 'c', 'd', 'e'],3))