import csv
import numpy as np
from DSAsorts import *

with open('RandomNames7000(2).csv', 'r') as csvfile:
    file = csv.reader(csvfile)
    ID = np.zeros(7000)

    i = 0
    for column in file:
        ID[i] = column[0]
        i += 1
    print(ID)




def main():
    bubbleSort(ID)
    with open('Bsort_ID_outputs.csv', 'a') as out:
        for i in ID:
            out.write(str(i))
    insertionSort(ID)
    with open('Isort_Id_outputs.csv', 'a') as out:
        for p in ID:
            out.write(str(p))
    selectionSort(ID)
    with open('Ssort_ID_outputs.csv', 'a') as out:
        for x in ID:
            out.write(str(x))


if __name__ == '__main__':
    main()
