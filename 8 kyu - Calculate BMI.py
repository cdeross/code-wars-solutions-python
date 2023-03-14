'''
Calculate BMI

Write function bmi that calculates body mass index (bmi = weight / height2).
if bmi <= 18.5 return "Underweight"
if bmi <= 25.0 return "Normal"
if bmi <= 30.0 return "Overweight"
if bmi > 30 return "Obese"
'''

def bmi(weight, height):
    bmi_person = weight / (height**2)
    if bmi_person <= 18.5:
        return "Underweight"
    elif 18.5 <= bmi_person <= 25.0:
        return "Normal"
    elif 25.0 <= bmi_person <= 30.0:
        return "Overweight"
    else:
        return "Obese"