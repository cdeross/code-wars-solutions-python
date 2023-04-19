'''
Predict your age!

My grandfather always predicted how old people would get, and right before he passed away he revealed his secret!
In honor of my grandfather's memory we will write a function using his formula!
Take a list of ages when each of your great-grandparent died.
Multiply each number by itself.
Add them all together.
Take the square root of the result.
Divide by two.
Example

predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86
Note: the result should be rounded down to the nearest integer.
'''


def predict_age(a1, a2, a3, a4, a5, a6, a7, a8):
    return int(((((a1**2) + (a2**2) + (a3**2) + (a4**2) + (a5**2) + (a6**2) + (a7**2) + (a8**2))**(1/2))/2)//1)



print(predict_age(65,60,75,55,60,63,64,45))

