'''
Century From Year

The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up
to and including the year 200, etc.
Task

Given a year, return the century it is in.
Examples

1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
Note: this kata uses strict construction as shown in the description and the examples, you can read more about it here
'''

def century(year):
    str_year = str(year)
    arr = []
    for c in str_year:
        arr.append(c)
    if len(str_year) == 1 or len(str_year) == 2:
        return 1
    elif len(str_year) == 3:
        if arr[-1] == '0' and arr[-2] == '0':
            return int(str(year)[:1]) -1
        elif arr[-1] == '0' and arr[-2] != '0':
            return int(str(year)[:1]) + 1
        else:
            return int(str(year)[:1]) + 1
    else:
        if arr[-1] == '0' and arr[-2] == '0':
            return int(str(year)[:2])
        elif arr[-1] == '0' and arr[-2] != '0':
            return int(str(year)[:2]) + 1
        else:
            return int(str(year)[:2]) + 1