'''
Reversing Words in a String

You need to write a function that reverses the words in a given string. A word can also fit an empty string.
 If this is not clear enough, here are some examples:
As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
Example (Input --> Output)
"Hello World" --> "World Hello"
"Hi There." --> "There. Hi"
'''

def reverse(st):
    i = 1
    sen = ""
    arr = st.split(" ")
    while len(arr) - i >= 0:
        if arr[-i] == "":
            i += 1
        else:
            sen = sen + " " + arr[-i]
            i += 1
    return sen[1:]