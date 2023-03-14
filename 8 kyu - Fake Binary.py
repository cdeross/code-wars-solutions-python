'''
Fake Binary

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
Return the resulting string.
Note: input will never be an empty string

'''

def fake_bin(x):
    number = ""
    for num in x:
        if int(num) < 5:
            number = number + "0"
        else:
            number = number + "1"
    return number