'''
Build Tower

Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.
For example, a tower with 3 floors looks like this:
[
  "  *  ",
  " *** ",
  "*****"
]
And a tower with 6 floors looks like this:
[
  "     *     ",
  "    ***    ",
  "   *****   ",
  "  *******  ",
  " ********* ",
  "***********"
]
'''

def tower_builder(n_floors):
    bottom_count = 1
    arr = []
    count = 0
    for i in range(n_floors - 1): #get the number of stars on the bottom level
        bottom_count += 2
    for i in range(n_floors):
        level = ""
        for j in range(bottom_count): #build pyrimid from bottom up
            level += "*"
        if count > 0:
            for k in range(count):
                level = " " + level + " " #add the appropriate nuber of spaces to make it line up properily
        bottom_count -= 2
        count += 1
        arr.append(level)
    return list(reversed(arr))