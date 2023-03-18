'''
Dashatize it

Given a variable n,
If n is an integer, Return a string with dash'-'marks before and after each odd integer, but do not begin or end the
string with a dash mark. If n is negative, then the negative sign should be removed.
If n is not an integer, return the string "None".
Ex:
dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
'''

def dashatize(n):
    res = ""
    if type(n) != int:
        return "None"
    else:
        strng = str(abs(n))
        for i in strng:
            if int(i) % 2 != 0:
                if len(res) > 1 and res[-1] == "-":
                    res = res + i + "-"
                else:
                    res = res + "-" + i + "-"
            else:
                res = res + i
    if res[0] == "-":
        res = res[1:]
    if res[-1] == "-":
        res = res = res[:-1]
    return str(res)



print(dashatize(86320))