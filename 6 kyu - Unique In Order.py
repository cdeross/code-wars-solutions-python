'''
Unique In Order

Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any
elements with the same value next to each other and preserving the original order of elements.
For example:
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
'''

def unique_in_order(sequence):
    seq = []
    arr = []
    if sequence == "" or sequence == [] or sequence == ():
        return []
    if type(sequence) == str:
        for i in sequence:
            seq.append(i)
    else:
        seq = sequence
    arr.insert(0, sequence[0])
    for i in seq[1:]:
        if i != arr[-1]:
            arr.append(i)
    return arr