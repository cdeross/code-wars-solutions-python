'''
Exclamation marks series #11

Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.
Examples

replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"
replace("aeiou") === "!!!!!"
replace("ABCDE") === "!BCD!"
'''

def replace_exclamation(s):
    sen = ""
    for i in s:
        if i in "aeiouAEIOU":
            i = i.replace(i, "!")
            print(i)
            sen = sen + i
        else:
            sen =  sen + i
    return sen