'''
Template Strings

Template Strings, this kata is mainly aimed at the new JS ES6 Update introducing Template Strings
Your task is to return the correct string using the Template String Feature.
Input:
Two Strings, no validation is needed.
Output:
You must output a string containing the two strings with the word ```' are '```
'''

from string import Template

def temple_strings(obj, feature):
    t = Template('$object are $feature')
    return (t.substitute(object = obj, feature = feature))