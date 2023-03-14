'''
Simple Encryption #1 - Alternating Split

Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.
Examples:
encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
Together with the encryption function, you should also implement a decryption function which reverses the process.
If the string S is an empty value or the integer N is not positive, return the first argument without changes.
This kata is part of the Simple Encryption Series:
Simple Encryption #1 - Alternating Split
Simple Encryption #2 - Index-Difference
Simple Encryption #3 - Turn The Bits Around
Simple Encryption #4 - Qwerty
Have fun coding it and please don't forget to vote and rank this kata! :-)
'''

def encrypt(encrypted_text, n):
    count = 0
    text = encrypted_text
    sen = ""
    while count < n:
        odds = ""
        evens = ""
        for i, j in enumerate(text):
            if i % 2 == 0:
                evens = evens + j
            else:
                odds = odds + j
            sen = odds + evens
        text = sen
        count += 1
    return text

def decrypt(text, n):
    if n <= 0 or not text:
        return text
    text =  list(text)
    length =  len(text)
    for i in range(n):
        odds = text[:length//2]
        evens = text[length//2:]
        for j in range(1, length, 2):
            k = odds.pop(0)
            evens.insert(j, k)
        text = evens
    return "".join(evens)