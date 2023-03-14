'''
Count characters in your string

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result
 should be {'a': 2, 'b': 1}.
What if the string is empty? Then the result should be empty object literal, {}.
'''

def count(string):
    dict = {}
    for i in string:
        if i in dict.keys():
            pass
        else:
            dict.update({i:string.count(i)})
    return dict