'''
Convert number to reversed array of digits

Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
Example(Input => Output):

35231 => [1,3,2,5,3]
0 => [0]
'''

def digitize(n):
    str_n = str(n)
    arr = []
    i = 0
    j = -1
    for a in str_n:
        arr.append(a)
    while i < (len(str_n)/2):
        fwd = arr[j]
        bwd = arr[i]
        arr[i] = int(fwd)
        arr[j] = int(bwd)
        i = i + 1
        j = j - 1
    return arr