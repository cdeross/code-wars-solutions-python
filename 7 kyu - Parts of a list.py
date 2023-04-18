'''
Parts of a list

Write a function partlist that gives all the ways to divide a list (an array) of at least two elements into two
non-empty parts.
Each two non empty parts will be in a pair (or an array for languages without tuples or a structin C - C:
see Examples test Cases - )
Each part will be in a string
Elements of a pair must be in the same order as in the original array.
Examples of returns in different languages:

a = ["az", "toto", "picaro", "zone", "kiwi"] -->
[["az", "toto picaro zone kiwi"], ["az toto", "picaro zone kiwi"], ["az toto picaro", "zone kiwi"],
["az toto picaro zone", "kiwi"]]
'''

def partlist(arr):
    output = []
    for i, j in enumerate(arr):
        if i == len(arr)-1:
            break
        else:
            output.append((" ".join(arr[:i+1]), " ".join(arr[i+1:])))
    return output