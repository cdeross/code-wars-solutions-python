'''
Row Weights

Given an array of positive integers (the weights of the people), return a new array/tuple of two integers,
where the first one is the total weight of team 1, and the second one is the total weight of team 2.
Notes

Array size is at least 1.
All numbers will be positive.
Input >> Output Examples

rowWeights([13, 27, 49])  ==>  return (62, 27)
Explanation:

The first element 62 is the total weight of team 1, and the second element 27 is the total weight of team 2.
rowWeights([50, 60, 70, 80])  ==>  return (120, 140)
Explanation:

The first element 120 is the total weight of team 1, and the second element 140 is the total weight of team 2.
rowWeights([80])  ==>  return (80, 0)
'''

def row_weights(array):
    team1 = 0
    team2 = 0
    arr = ()
    for i, j in enumerate(array):
        if i % 2 != 0:
            team2 = team2 + j
        else:
            team1 = team1 + j
    arr = arr + (team1, team2)
    return arr