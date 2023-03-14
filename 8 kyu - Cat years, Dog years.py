'''
Cat years, Dog years

I have a cat and a dog.
I got them at the same time as kitten/puppy. That was humanYears years ago.
Return their respective ages now as [humanYears,catYears,dogYears]
NOTES:
humanYears >= 1
humanYears are whole numbers only
Cat Years

15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that
Dog Years

15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that
'''

def human_years_cat_years_dog_years(human_years):
    arr = [human_years]
    dog_years = 0
    cat_years = 0
    i =0
    if human_years == 1:
        cat_years += 15
        dog_years += 15
        arr.append(cat_years)
        arr.append(dog_years)
    if human_years == 2:
        cat_years += 24
        dog_years += 24
        arr.append(cat_years)
        arr.append(dog_years)
    if human_years >=3:
        n = human_years - 2
        while i < n:
            dog_years += 5
            cat_years += 4
            i += 1
        dog_years += 24
        cat_years += 24
        arr.append(cat_years)
        arr.append(dog_years)
    return arr