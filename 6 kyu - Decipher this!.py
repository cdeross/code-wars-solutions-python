'''
Decipher this!

You are given a secret message you need to decipher. Here are the things you need to know to decipher it:
For each word:
the second and the last letter is switched (e.g. Hello becomes Holle)
the first letter is replaced by its character code (e.g. H becomes 72)
Note: there are no special characters used, only letters and spaces

Examples
decipherThis('72olle 103doo 100ya'); // 'Hello good day'
decipherThis('82yade 115te 103o'); // 'Ready set go'
'''

def decipher_this(s):
    output = ""
    arr = s.split()
    for i in arr:
        word = ""
        num = ""
        w = ""
        for j in i:
            if j.isnumeric() == True:
                num += j
            else:
                w += j
        if w == "":
            word = chr(int(num))
        else:
            word = chr(int(num)) + w[-1] + w[1:-1] + w[0]
            if len(w) == 1:
                word = word[:-1]
        output += word + " "
    return output[:-1]