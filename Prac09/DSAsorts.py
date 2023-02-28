#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

from pandas import array
import numpy as np
import random


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
    return mergeSortRecurse(A, 0, len(A)-1)


def mergeSortRecurse(A, leftIdx, rightIdx):
    if leftIdx < rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        mergeSortRecurse(A, leftIdx, midIdx)
        mergeSortRecurse(A, midIdx + 1, rightIdx)
        merge(A, leftIdx, midIdx, rightIdx)
    return A


def merge(A, leftIdx, midIdx, rightIdx):
    """ merge - merge two sorted sub-arrays into one sorted array
    """
    tempArr = np.zeros(rightIdx - leftIdx + 1)
    ii = leftIdx
    jj = midIdx + 1
    kk = 0
    while ii <= midIdx and jj <= rightIdx:
        if A[ii] < A[jj]:
            tempArr[kk] = A[ii]
            ii += 1
        else:
            tempArr[kk] = A[jj]
            jj += 1
        kk += 1
    for ii in range(ii, midIdx + 1):
        tempArr[kk] = A[ii]
        kk += 1
    for jj in range(jj, rightIdx + 1):
        tempArr[kk] = A[jj]
        kk += 1
    for kk in range(leftIdx, rightIdx + 1):
        A[kk] = tempArr[kk - leftIdx]


def quickSort(A, *, pivoting):
    return quickSortRecurse(A, 0, len(A) - 1, pivoting)


def quickSortRecurse(A, leftIdx, rightIdx, pivoting):
    if leftIdx < rightIdx:
        pivotIdx = pivoting(A, leftIdx, rightIdx)
        pivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        quickSortRecurse(A, leftIdx, pivotIdx - 1, pivoting)
        quickSortRecurse(A, pivotIdx + 1, rightIdx, pivoting)


def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    pivotVal = A[pivotIdx]
    A[pivotIdx] = A[rightIdx]
    A[rightIdx] = pivotVal
    currIdx = leftIdx
    for ii in range(leftIdx, rightIdx):
        if A[ii] < pivotVal:
            temp = A[ii]
            A[ii] = A[currIdx]
            A[currIdx] = temp
            currIdx += 1
    temp = A[currIdx]
    A[currIdx] = A[rightIdx]
    A[rightIdx] = temp
    return currIdx


def leftMostPivot(A, leftIdx, rightIdx):
    return leftIdx


def pivot3Median(A, leftIdx, rightIdx):
    # Find median of 3 pivots
    midIdx = (leftIdx + rightIdx) // 2
    if A[leftIdx] <= A[midIdx] <= A[rightIdx] or A[rightIdx] <= A[midIdx] <= A[leftIdx]:
        pivotIdx = midIdx
    elif A[midIdx] <= A[leftIdx] <= A[rightIdx] or A[rightIdx] <= A[leftIdx] <= A[midIdx]:
        pivotIdx = leftIdx
    else:
        pivotIdx = rightIdx
    return pivotIdx


def QuickSortRandom(A):
    quickSort(A, pivoting=randomPivot)


def randomPivot(A, leftIdx, rightIdx):
    return random.randint(leftIdx, rightIdx)

# create table of runtime results using 4 array sizes and 3 sorting options for
# all implemented sorting algorithms, write a paragraph in terms of time complexity
# and other characteristics of sorting algorithms
