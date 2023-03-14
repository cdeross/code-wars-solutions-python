'''
Find the position!

When provided with a letter, return its position in the alphabet.
Input :: "a"
Ouput :: "Position of alphabet: 1"
'''


def position(alphabet):
    for i, j in enumerate("abcdefghijklmnopqrstuvwxyz"):
        if j == alphabet:
            return "Position of alphabet: {}".format(i + 1)