'''
Contamination #1 -String-

An AI has infected a text with a character!!
This text is now fully mutated to this character.
If the text or the character are empty, return an empty string.
There will never be a case when both are empty as nothing is going on!!
Note: The character is a string of length 1 or an empty string.

'''

def contamination(text, char):
    return "" if text == "" else "".join(char for i in range(1, len(text) +1))