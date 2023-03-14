'''
Isograms

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that
determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram.
Ignore letter case.
Example: (Input --> Output)
"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)
isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false
'''

def is_isogram(string):
    i = 0
    while i < len(string):
        word = string[:i] + string[i + 1:]
        if string[i].lower() in word.lower():
            return False
            break
        else:
            i += 1
    return True