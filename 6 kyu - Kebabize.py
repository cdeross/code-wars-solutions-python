'''
Kebabize

Modify the kebabize function so that it converts a camel case string into a kebab case.
"camelsHaveThreeHumps"  -->  "camels-have-three-humps"
"camelsHave3Humps"  -->  "camels-have-humps"
"CAMEL"  -->  "c-a-m-e-l"
Notes:
the returned string should only contain lowercase letters
'''

def kebabize(st):
    res = ""
    for j, i in enumerate(st):
        if i.isupper() and j !=0:
            res = res + "-" + i
        else:
            if i.isalpha():
                res = res + i
            else:
                res = res + ""
    if len(res) > 0 and res[0] == "-":
        res = res[1:]
    return res.lower()

