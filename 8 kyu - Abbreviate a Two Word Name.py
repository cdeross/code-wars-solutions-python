'''
Abbreviate a Two Word Name

Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
It should look like this:
Sam Harris => S.H
patrick feeney => P.F
'''

def abbrev_name(name):
    i = 0
    space = 0
    initials = ""
    while i < len(name):
        if i == 0:
            initials = name[0] + "."
            i += 1
        else:
            if space == 1:
                initials = initials + name[i]
                break
            else:
                if name[i] == " ":
                    space += 1
                    i += 1
                else:
                    i += 1
    return initials.upper()