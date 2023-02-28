#
# Gcd_numCon.py - recursive greatest common divisor and number conversion algorithm
#

def gcd_Wrap(a, b):
    if a and b < 0:
        raise ValueError('Import must not be negative')
    else:
        return _gcd_Re(a, b)


def _gcd_Re(a, b):
    if (b == 0):
        return a
    else:
        return _gcd_Re(b, a % b)

# Source, my own implementation of the gcd algorithm


def decToBase_Wrap(dec, base):
    if dec and base < 0:
        raise ValueError('Dec and base  must not be negative')
    elif 16 > base < 2:
        raise ValueError('Base must be between 2 and 16')
    else:
        return _decToBase_Re(dec, base)


def _decToBase_Re(dec, base):
    if (dec == 0):
        return ''
    else:
        return _decToBase_Re(dec//base, base) + str(dec % base)

# Source, my own implementation of the base conversion algorithm


def main():
    print(gcd_Wrap(10, 5))
    print(decToBase_Wrap(10, 2))
    print('Done')


if __name__ == '__main__':
    main()

# Prac02 completed
