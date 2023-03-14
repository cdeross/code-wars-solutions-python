'''
Rot13

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the
alphabet. ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet
should be shifted, like in the original Rot13 "implementation".
Please note that using encode is considered cheating.

'''

dict = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14,
            "o":15, "p":16, "q":17, "r":18, 's':19, "t":20, "u":21, "v": 22, "w":23, "x": 24, "y":25, "z":26}

def rot13(message):
    uppercase = False
    secret_msg = ""
    for i in message:
        if i not in dict and i.isalpha() != True:
            secret_msg = secret_msg + i
        else:
            if i.isupper() == True:
                uppercase = True
            i = i.lower()
            new_num = dict.get(i) + 13
            if new_num > 26:
                new_num = new_num - 26
            if uppercase == True:
                secret_msg = secret_msg + list(dict.keys())[list(dict.values()).index(new_num)].upper()
                uppercase = False
            else:
                secret_msg = secret_msg + list(dict.keys())[list(dict.values()).index(new_num)]
    return secret_msg