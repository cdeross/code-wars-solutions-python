'''
Alternate capitalization

Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below.
 Index 0 will be considered even.
For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.
The input will be a lowercase string with no spaces.
Good luck!
If you like this Kata, please try:
Indexed capitalization
Even-odd disparity
'''

def capitalize(s):
    arr = []
    word1 = ""
    word2 = ""
    for i,j in enumerate(s):
        if i % 2 == 0:
            word1 = word1 + j.upper()
            word2 = word2 + j
        else:
            word1 = word1 + j
            word2 = word2 + j.upper()
    arr.append(word1)
    arr.append(word2)
    return arr