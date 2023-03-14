'''
The Vowel Code

Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers
according to the following pattern:
a -> 1
e -> 2
i -> 3
o -> 4
u -> 5
For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.
Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern
shown above.
For example, decode("h3 th2r2") would return "hi there".
For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.
'''

dict1 = {"a":"1", "e":"2", "i":"3", "o":"4", "u":"5"}

def encode(st):
    word = ""
    for i in st:
        if i in dict1:
            word = word + dict1.get(i)
        else:
            word = word + i
    return word

def decode(st):
    word = ""
    dict2 = {value: key for key, value in dict1.items()}
    for i in st:
        if i in dict2:
            word = word + dict2.get(i)
        else:
            word = word + i
    return word