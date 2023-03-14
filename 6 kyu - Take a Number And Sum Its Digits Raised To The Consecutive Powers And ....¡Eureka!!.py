'''
Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!

The number 89
89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this
 kata. What's the use of saying "Eureka"? Because this sum gives the same number:


'''

def sum_dig_pow(a, b):
    sum = 0
    arr = []
    for i in range(a, b +1):
        for j, k in enumerate(str(i)):
            sum = sum + int(k)**(j+1)
        if sum == i:
            arr.append(i)
            sum = 0
        else:
            sum = 0
    return arr