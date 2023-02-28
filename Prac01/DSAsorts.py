#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

from pandas import array


def bubbleSort(A):
    for p in range(len(A)-1):
        for ii in range(len(A)-1 - p):
            if A[ii] > A[ii+1]:
                temp = A[ii]
                A[ii] = A[ii+1]
                A[ii + 1] = temp


def insertionSort(A):
    for nn in range(len(A)-1):
        ii = nn
        while ii > 0 and A[ii] < A[ii-1]:
            temp = A[ii]
            A[ii] = A[ii-1]
            A[ii-1] = temp
            ii -= 1

def selectionSort(A):
    for nn in range(len(A)-1):
        minIdx = nn
        for ii in range(nn+1, len(A)-1):
            if A[ii] < A[minIdx]:
                minIdx = ii
        temp = A[minIdx]
        A[minIdx] = A[nn]
        A[nn] = temp


def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...


def mergeSortRecurse(A, leftIdx, rightIdx):
    if leftIdx < rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        mergeSortRecurse(A, leftIdx, midIdx)
        mergeSortRecurse(A, midIdx + 1, rightIdx)
        merge(A, leftIdx, midIdx, rightIdx)
    return A


def merge(A, leftIdx, midIdx, rightIdx):
    ...


def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...


def quickSortRecurse(A, leftIdx, rightIdx):
    ...


def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...
