'''
Name Shuffler

Write a function that returns a string in which firstname is swapped with last name.
Example(Input --> Output)
"john McClane" --> "McClane john"
'''

def name_shuffler(str_):
    arr = str_.split(" ")
    return "{} {}".format(arr[1], arr[0])