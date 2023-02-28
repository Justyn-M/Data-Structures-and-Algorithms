#
# Fac_Fib.py - Calculate the factorial and fibonacci numbers using iterative and recursive methods
#

from multiprocessing.sharedctypes import Value

# Wrapper


def calcFactorial(n):
    if n < 0:
        raise ValueError('Import must not be negative')
    else:
        return _calcFactorialRecursive(n)

# Method


def _calcFactorialRecursive(n):
    if (n == 0):
        factorial = 1
    else:
        factorial = n * _calcFactorialRecursive(n-1)
    return factorial

# fibonacci algorithm wrapper


def fib_Rewrap(n):
    if n < 0:
        raise ValueError('Import must not be negative')
    else:
        return _fibRecursive(n)


def fib_Itwrap(n):
    if n < 0:
        raise ValueError('Import must not be negative')
    else:
        return _fibIterative(n)


def _fibIterative(n):
    fibVal = 0
    currVal = 1
    lastVal = 0

    if (n == 0):
        fibVal = 0
    elif (n == 1):
        fibVal = 1
    else:
        for ii in range(2, n+1):
            fibVal = currVal + lastVal
            lastVal = currVal
            currVal = fibVal
    return fibVal


def _fibRecursive(n):
    fibVal = 0

    if (n == 0):
        fibVal = 0
    elif (n == 1):
        fibVal = 1
    else:
        fibVal = _fibRecursive(n-1) + _fibRecursive(n-2)
    return fibVal


def main():
    print(calcFactorial(10))
    print(fib_Itwrap(10))
    print(fib_Rewrap(10))
    print('Done')


if __name__ == '__main__':
    main()
