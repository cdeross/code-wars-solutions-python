'''
Mumbling

This time no story, no theory. The examples below show you how to write function accum:
Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
'''

def accum(s):
    mumble = ""
    i = 0
    for i in range(0, len(s)):
        for j in range(1, i+2):
            if j == 1:
                if j == i+1:
                    mumble = mumble + s[i].upper() + "-"
                else:
                    mumble = mumble + s[i].upper()
            else:
                if j == i+1:
                    mumble = mumble + s[i].lower() + "-"
                else:
                    mumble = mumble + s[i].lower()

    return mumble[:-1]