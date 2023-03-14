'''
Detect Pangram

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence
"The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once
(case is irrelevant).
Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
'''

def is_pangram(s):
    sen = s.lower()
    sen = "".join(i for i in sen if i.isalpha())
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for s in sen:
        if s in alpha:
            alpha = alpha.replace(s, "")
            if len(alpha) == 0:
                return True
            else:
                pass
    return False