'''
Parse float

Write function parse_float which takes a string/list and returns a number or 'none' if conversion is not possible.
'''

def parse_float(string):
    try:
        float(string)
        return float(string)
    except ValueError:
        return None
    except TypeError:
        return None