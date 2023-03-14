'''
Exes and Ohs

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case
insensitive. The string can contain any char.
Examples input/output:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
'''

def xo(s):
    arr = []
    for d in s:
        arr.append(d)
    i = 0
    x_cnt = 0
    o_cnt = 0
    while i < len(arr):
        if arr[i].lower() == 'x':
            x_cnt = x_cnt + 1
            i = i +1
        elif arr[i].lower() == 'o':
            o_cnt = o_cnt +1
            i = i + 1
        else:
            i = i +1
    if x_cnt == 0 and o_cnt == 0:
        return True
    elif x_cnt == o_cnt:
        return True
    else:
        return False