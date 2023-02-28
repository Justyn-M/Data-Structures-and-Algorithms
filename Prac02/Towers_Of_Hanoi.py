#
# Towers_Of_Hanoi.py - Towers of Hanoi algorithm
#

def towers_of_hanoi(n, src, dest):
    if n == 1:
        moveDisk(src, dest)
    else:
        temp = 6 - src - dest
        towers_of_hanoi(n-1, src, temp)
        moveDisk(src, dest)
        towers_of_hanoi(n-1, temp, dest)


def moveDisk(src, dest):
    print("Move disk from tower", src, "to tower", dest)
    print("\t", end="")


def main():
    towers_of_hanoi(3, 1, 3)


if __name__ == '__main__':
    main()