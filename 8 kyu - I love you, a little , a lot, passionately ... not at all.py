'''
I love you, a little , a lot, passionately ... not at all

Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of
 the following phrases each time a petal was torn:
"I love you"
"a little"
"a lot"
"passionately"
"madly"
"not at all"
If there are more than 6 petals, you start over with "I love you" for 7 petals, "a little" for 8 petals and so on.
When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.
Your goal in this kata is to determine which phrase the girls would say at the last petal for a flower of a given
number of petals. The number of petals is always greater than 0.
'''

def how_much_i_love_you(nb_petals):
    if nb_petals % 6 == 0:
        return "not at all"
    if nb_petals % 6 == 1:
        return "I love you"
    if nb_petals % 6 == 2:
        return "a little"
    if nb_petals % 6 == 3:
        return "a lot"
    if nb_petals % 6 == 4:
        return "passionately"
    if nb_petals % 6 == 5:
        return "madly"
    if nb_petals % 6 == 6:
        return "not at all"