'''
Word a10n (abbreviation)

The word i18n is a common abbreviation of internationalization in the developer community, used instead of typing the
whole word and trying to spell it correctly. Similarly, a11y is an abbreviation of accessibility.
Write a function that takes a string and turns any and all "words" (see below) within that string of length 4 or greater
 into an abbreviation, following these rules:
A "word" is a sequence of alphabetical characters. By this definition, any other character like a space or hyphen
(eg. "elephant-ride") will split up a series of letters into two words (eg. "elephant" and "ride").
The abbreviated version of the word should have the first letter, then the number of removed characters, then the last
letter (eg. "elephant ride" => "e6t r2e").
Example

abbreviate("elephant-rides are really fun!")
//          ^^^^^^^^*^^^^^*^^^*^^^^^^*^^^*
// words (^):   "elephant" "rides" "are" "really" "fun"
//                123456     123     1     1234     1
// ignore short words:               X              X

// abbreviate:    "e6t"     "r3s"  "are"  "r4y"   "fun"
// all non-word characters (*) remain in place
//                     "-"      " "    " "     " "     "!"
=== "e6t-r3s are r4y fun!"
'''


def abbreviate(s):
    word = ""
    res = []
    word_position = 0
    sen = s.split(" ")
    sentence = []

    #check for special charecters
    for i, j in enumerate(sen):
        if j[-1].isalpha():
            sentence.append(j)
        else:
            sentence.append(j[0:-1])
            sentence.append(j[-1:])

    #remove "-" from word and add to
    for i, j in enumerate(sentence):
        if "-" in j:
            del sentence[i]
            word = j.split("-")
            for k in range(len(word)):
                sentence.insert(k + i, word[k])
            word_position = i

    for i, j in enumerate(sentence):
        if j.isalpha():
            count = 0
            count = len(j) - 2
            if count > 1 and len(sentence) > 1:
                if i == word_position:
                    res.append(sentence[i][0] + str(count) + sentence[i][-1] + "-" + sentence[i+1][0] + str(len(sentence[i+1]) - 2) + sentence[i+1][-1])
                    del sentence[i+1]
                else:
                    res.append(str(j[0]) + str(count) + str(j[len(j)-1]))
            elif len(sentence) == 1:
                res.append(str(j[0]) + str(count) + str(j[len(j) - 1]))
            else:
                res.append(j)
        else:
            res.append(j)
    result =[]
    #add back special charecters
    for i, j in enumerate(res):
        if j in "~`!@#$%^&*()_+={[}]|:;<,>.?/":
            result.append(res[i-1] + res[i])
            if i > 2:
                del result[i - 2]
            else:
                del result[i-1]
        else:
            result.append(j)
    return ' '.join(i for i in result)