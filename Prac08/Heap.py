#
# Heap.py - Heap data structure
#

import numpy as np
import csv
from typing import List, Tuple


class HeapEntry():
    def __init__(self, priority: int, value: object):
        self._priority = priority
        self._value = value

    @property
    def priority(self):
        return self._priority

    @property
    def value(self):
        return self._value

    @priority.setter
    def priority(self, key: int):
        self._priority = key

    @value.setter
    def value(self, val: int):
        self._value = val


class DSAHeap:
    def __init__(self, size: int = 100):
        self._heap = np.zeros(size, dtype=HeapEntry)
        self._count = 0

        for i in range(len(self._heap)):
            self._heap[i] = HeapEntry(0, None)

    def add(self, priority, value):
        if self._count == len(self._heap):
            raise ValueError('Heap has reached max capacity')
        else:
            self._heap[self._count].priority = priority
            self._heap[self._count].value = value
            self.trickleUp(self._count)
            self._count += 1

    def remove(self):
        down = 0
        if self._count == 0:
            raise ValueError("Heap is empty.")
        else:
            self._count -= 1
            value = self._heap[down].value
            self._heap[down], self._heap[self._count] = self._heap[self._count], self._heap[down]
            self.trickleDown(down)
        return value

    def trickleUp(self, index):
        parentIdx = int((index - 1) / 2)
        if index > 0 and self._heap[parentIdx].priority < self._heap[index].priority:
            self._heap[parentIdx], self._heap[index] = self._heap[index], self._heap[parentIdx]
            self.trickleUp(parentIdx)

    def trickleDown(self, index):
        leftChildIdx = index * 2 + 1
        rightChildIdx = leftChildIdx + 1
        swap = 0
        if leftChildIdx < self._count:
            swap = leftChildIdx
        if rightChildIdx < self._count and self._heap[rightChildIdx].priority > self._heap[leftChildIdx].priority:
            swap = rightChildIdx
        if swap != 0 and self._heap[swap].priority > self._heap[index].priority:
            self._heap[swap], self._heap[index] = self._heap[index], self._heap[swap]
            self.trickleDown(swap)

    def heapify(self):
        start = int((len(self) - 2) / 2)
        for i in reversed(range(start + 1)):
            self.trickleDown(i)

    @staticmethod
    def heapSort(values: List[Tuple[int, object]]) -> List[Tuple[int, object]]:
        heap = DSAHeap(len(values))
        for i in range(len(values)):
            heap._heap[i].priority = values[i][0]
            heap._heap[i].value = values[i][1]
        heap._count = len(values)
        heap.heapify()
        for i in reversed(range(1, heap._count)):
            heap._heap[0], heap._heap[i] = heap._heap[i], heap._heap[0]
            heap._count -= 1
            heap.trickleDown(0)
        return [(x.priority, x.value) for x in heap._heap]

    def __len__(self):
        return self._count

    def __iter__(self):
        def iterate(heap):
            for i in range(self._count):
                yield heap._heap[i]
        return iterate(self)


# test code
if __name__ == "__main__":
    heap = DSAHeap(10)
    heap.add(1, "one")
    heap.add(2, "two")
    heap.add(3, "three")
    heap.add(4, "four")
    heap.add(5, "five")
    heap.add(6, "six")
    heap.add(7, "seven")
    heap.add(8, "eight")
    heap.add(9, "nine")
    heap.add(10, "ten")
    for i in heap:
        print(i.priority, i.value)
    print("Removing...")
    for i in range(10):
        print(heap.remove())
    print("End of heap sort test")

    print('==============')

# read from csv file
    with open('RandomNames7000.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    data = [(int(x[0]), x[1]) for x in data]
    print('Reading from csv file...')
    print('Successfully read names, sorting to output csv file...')

# write to csv file
    with open('SortedNames7000.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(DSAHeap.heapSort(data))

    print('==============')
    print('Successfully sorted names, output to csv file.')
