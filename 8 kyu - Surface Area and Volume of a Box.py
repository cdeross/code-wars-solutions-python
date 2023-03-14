'''
Surface Area and Volume of a Box

Write a function that returns the total surface area and volume of a box as an array: [area, volume]
'''

def get_size(w,h,d):
    return [(((w*h)*2) +((h*d)*2) +((w*d)*2)), w*h*d]