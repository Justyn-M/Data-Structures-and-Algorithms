#**
#** Testharness to generate various different types of arrays of integers
#** and then sort them using various sorts.
#**
#** Each sort is run REPEATS times, with the first result discarded,
#** and the last REPEATS-1 runs averaged to give the running time.
#**
#** Author of java version: Andrew Turpin (andrew@cs.curtin.edu.au)
#** Date:    August 2004
#** Modified (java): Patrick Peursum
#** Date:     Sep 2009
#** Modified (python): Valerie Maxville
#** Date:    August 2017
#** Modified (python): Hayden Richards
#** Date:    March 2018

import numpy as np
import sys
import timeit
import DSAsorts
import random


REPEATS = 3           #No times to run sorts to get mean time
NEARLY_PERCENT = 0.10 #% of items to move in nearly sorted array
RANDOM_TIMES = 100    #No times to randomly swap elements in array

def usage():
    print(" Usage: java TestHarness n xy [xy ...]")
    print("        where")
    print("        n is number of integers to sort")
    print("        x is one of")
    print("           b - bubblesort")
    print("           i - insertion sort")
    print("           s - selection sort")
    print("           q - quicksort")
    print("           m - mergesort")
    print("        y is one of")
    print("           a - 1..n ascending")
    print("           d - 1..n descending")
    print("           r - 1..n in random order")
    print("           n - 1..n nearly sorted (10% moved)")

def doSort(n, sortType, arrayType):
        A = np.arange(1, n+1, 1)   #create array with values from 1 to n
        
        if arrayType == 'a':
            ...
        elif arrayType =='d':  #convert to descending
            for i in range(0, int(n/2)):
                temp = A[i]
                A[i] = A[n-i-1]
                A[n-i-1] = temp
            print("Descending: ", A)
        elif arrayType == 'r':
            for i in range(RANDOM_TIMES*n):
                x = int(random.random()*n)
                y = int(random.random()*n)
                temp = A[x]
                A[x] = A[y]
                A[y] = temp
            print("Random: ", A)
        elif arrayType == 'n':
            for i in range(int(n*NEARLY_PERCENT/2+1)):
                x = int(random.random()*n)
                y = int(random.random()*n)
                temp = A[x]
                A[x] = A[y]
                A[y] = temp
            print("Nearly sorted: ", A)
        else:
            print("Unsupported array type")

        if sortType == "b":
            DSAsorts.bubbleSort(A)
        elif sortType == "s":
            DSAsorts.selectionSort(A)
        elif sortType == "i":
            DSAsorts.insertionSort(A)
        elif sortType == "m":
            DSAsorts.mergeSort(A)
        elif sortType == "q":
            DSAsorts.quickSort(A)
        else:
            print("Unsupported sort algorithm")

        for i in range(n-2):
            if (A[i] > A[i+1]):
                raise ValueError("Array not in order")

#main program

if len(sys.argv) < 3:
    usage()
else:
    for aa in range(2, len(sys.argv)):
        
        n = int(sys.argv[1])
        sortType = sys.argv[aa][0]
        arrayType = sys.argv[aa][1]

        runningTotal = 0

        for repeat in range(REPEATS):
             startTime = timeit.default_timer()
             doSort(n, sortType, arrayType)
             endTime = timeit.default_timer()

             runningTotal += (endTime - startTime)
    
        print(sortType + arrayType + " " + str(n) + " " + str(runningTotal/(REPEATS - 1)))
