'''
Disemvowel Trolls

Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the
threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.
'''

def disemvowel(string_):
    phrase = ""
    is_upper = False
    for s in string_:
        if s.isupper() == True:
            is_upper = True
        else:
            is_upper = False
        s = s.lower()
        if s == "a" or s == "e" or s == "i" or s == "o" or s == "u":
            pass
        else:
            if is_upper == True:
                phrase = phrase + s.upper()
                is_upper = False
            else:
                phrase = phrase + s
    return phrase