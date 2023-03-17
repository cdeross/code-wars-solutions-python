'''
Ordered Count of Characters

Count the number of occurrences of each character and return it as a (list of tuples) in order of appearance.
For empty output return (an empty list).
Consult the solution set-up for the exact data structure implementation depending on your language.

Example:
ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
'''

def ordered_count(inp):
    res = []

    for i in inp:
        x = inp.count(i)
        if (i, x) not in res:
            res.append((i, x))
    return res





print(ordered_count("abracadabra"))