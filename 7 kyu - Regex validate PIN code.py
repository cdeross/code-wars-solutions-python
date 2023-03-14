'''
Regex validate PIN code

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6
digits.
If the function is passed a valid PIN string, return true, else return false.
Examples (Input --> Output)

"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
'''

def validate_pin(pin):
    if pin == '':
        return False
    else:
        for p in pin:
            if pin.isdigit() == False:
                return False
            else:
                if len(str(pin)) == 4 or len(str(pin)) == 6:
                    return True
                else:
                    return False