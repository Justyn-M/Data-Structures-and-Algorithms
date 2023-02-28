#
# Q1gcdTest.py - Recursive greatest common denominator
# source: - My answer for a question in Practical 2 of DSA
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


if __name__ == '__main__':
    # Student ID - 21029112
    print(gcd_Wrap(2102, 9112))
    print(gcd_Wrap(9112, 2102))
