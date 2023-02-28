#
# HashTable.py - DSA hash table implementation
#

import numpy as np
# need np.empty() to create the DSAHashEntry array
from math import ceil
# need ceil for _next_prime() hash table size
from enum import Enum
# need Enum for using enumeration types to set the ,key, value state of the hash table
from math import sqrt


class DSAHashEntry:
    class HashState(Enum):
        EMPTY = -1
        OCCUPIED = 0
        MAX = 1

    def __init__(self, key=None, value: object = None,
                 state: "HashState" = HashState.EMPTY):
        self._key = key
        self._value = value
        self._state = state

# used decorations for setters

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

    @property
    def state(self):
        return self._state

    @key.setter
    def keyAllocate(self, key):
        self._key = key

    @value.setter
    def valueAllocate(self, value):
        self._value = value

    @state.setter
    def stateAllocate(self, state):
        self._state = state


class DSAHashTable:
    def __init__(self, size=100, *, loadminFactor=0,
                 loadmaxFactor=0.5, factorResize=2, _rResize=True):
        self._hashArray = np.empty(DSAHashTable._nextPrime(size), dtype=object)
        for i in range(len(self._hashArray)):
            self._hashArray[i] = DSAHashEntry()
            self._count = 0
            self._rResize = _rResize
            self._loadminFactor = loadminFactor
            self._loadmaxFactor = loadmaxFactor
            self._factorResize = factorResize

# ValueErrors that are raised when loadfactors are not met within conditions
        if (loadmaxFactor - loadminFactor < 1/3 and loadminFactor != 0
                or loadmaxFactor > 1 or loadminFactor < 0 or loadmaxFactor == 0):
            raise ValueError("Invalid max and min load factor.")
        if 1 > loadmaxFactor * factorResize or loadmaxFactor < loadminFactor * factorResize:
            raise ValueError("Invalid resize factor.")

# non static functions for Hash Table
    def put(self, key, value: object) -> None:
        hashed = self._find(key)
        if hashed is None or hashed.state != DSAHashEntry.HashState.MAX:
            self._count += 1
            if self._rResize:
                if self._Resizing():
                    hashed = self._find(key)
            hashed.stateAllocate = DSAHashEntry.HashState.MAX
            hashed.keyAllocate = key
            hashed.valueAllocate = value

    def get(self, key) -> DSAHashEntry:
        hashed = self._find(key)
        if hashed is None or hashed.state != DSAHashEntry.HashState.MAX:
            raise ValueError("Cannot find key")
        return hashed.value

    def hasKey(self, key) -> bool:
        hashed = self._find(key)
        return hashed is not None and hashed.state == DSAHashEntry.HashState.MAX

    def remove(self, key) -> object:
        hashed = self._find(key)
        if hashed is None or hashed.state != DSAHashEntry.HashState.MAX:
            raise ValueError("Cannot find key.")
        self._count -= 1
        if self._rResize:
            if self._Resizing():
                hashed = self._find(key)
        hashed.stateAllocate = DSAHashEntry.HashState.OCCUPIED
        hashed.keyAllocate = None
        value = hashed.valueAllocate
        hashed.valueAllocate = None
        return value

    def loadFactor(self) -> float:
        return len(self) / len(self._hashArray)

    def export(self) -> str:
        return "".join([f"{k},{v}\n" for (k, v) in self])

    def __len__(self):
        return self._count

    def _find(self, key) -> DSAHashEntry:
        i = DSAHashTable._hash(key, len(self._hashArray))
        stepHash = DSAHashTable._stepHash(key, len(self._hashArray))
        hashed = self._hashArray[i]
        jumps = 0
        while hashed.key != key and hashed.state != DSAHashEntry.HashState.EMPTY and jumps < len(self._hashArray):
            jumps += 1
            i = (i + stepHash) % len(self._hashArray)
            hashed = self._hashArray[i]

        if jumps == len(self._hashArray):
            hashed = None
        return hashed

    def _Resizing(self) -> bool:
        resized = False
        if self.loadFactor() > self._loadmaxFactor:
            self._resize(ceil(len(self._hashArray) * self._factorResize))
            resized = True
        elif self.loadFactor() < self._loadminFactor:
            self._resize(ceil(len(self._hashArray) / self._factorResize))
            self._resize(ceil(len(self) / self._loadmaxFactor))
            resized = True
        return resized

    def _resize(self, size):
        newTable = DSAHashTable(size, _rResize=False)
        for k, v in self:
            newTable.put(k, v)
        self._hashArray = newTable._hashArray

    def __iter__(self):
        def hashIter(hashArray):
            for x in hashArray:
                if x.state == DSAHashEntry.HashState.MAX:
                    yield (x.key, x.value)
        return hashIter(self._hashArray)

# static methods used for hash table
    @staticmethod
    def read(string: str) -> 'DSAHashTable':
        lines = string.split('\n')[:-1]
        table = DSAHashTable(len(lines))
        for x in lines:
            key, value = x.split(',')
            if not table.hasKey(key):
                table.put(key, value)
        return table

    @staticmethod
    def _hash(key, len: int) -> int:
        return DSAHashTable._HashStr(key) % len

    @staticmethod
    def _stepHash(key, len: int) -> int:
        return DSAHashTable._fowlerHash(key) % (len - 1) + 1

    @staticmethod
    def _packKey(key):
        import struct
        if isinstance(key, int):
            key = struct.pack("i", key)
        elif isinstance(key, str):
            key = key.encode()
        else:
            raise ValueError("Key type is invalid - Problem: Unsupported type")
        return key

    @staticmethod
    def _HashStr(key) -> int:
        key = DSAHashTable._packKey(key)
        hash = 0
        for i in range(len(key)):
            hash = (hash << 5) - hash + key[i]
        return hash

    @staticmethod
    def _fowlerHash(key) -> int:
        hash = 0
        for x in DSAHashTable._packKey(key):
            hash = hash * 0x01000193 ^ x
        return hash

    @staticmethod
    def _nextPrime(x: int) -> int:
        if x % 2 == 0:
            x += 1
        else:
            x += 2
        while not DSAHashTable._isPrime(x):
            x += 2
        return x

    @staticmethod
    def _isPrime(x: int) -> bool:
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        for i in range(3, ceil(sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
        return True


if __name__ == '__main__':
    import random
    import time

    def test():
        print("Testing DSAHashTable...")
        print('=======================')
        table = DSAHashTable(100)
        for i in range(100):
            table.put(i, i)
        print(f"Size of table: {len(table)}")
        for i in range(100):
            assert table.get(i) == i
        for i in range(100):
            assert table.hasKey(i)
        for i in range(100):
            assert table.remove(i) == i
        print(f"Size of table: {len(table)}")
        for i in range(100):
            assert not table.hasKey(i)
        print("Done.")

    def benchmark():
        print("Benchmarking DSAHashTable...")
        print('============================')
        table = DSAHashTable(100)
        start = time.time()
        for i in range(100000):
            table.put(i, i)
        end = time.time()
        print(f"Insertion: {end - start}s")
        start = time.time()
        for i in range(100000):
            table.get(i)
        end = time.time()
        print(f"Retrieval: {end - start}s")
        start = time.time()
        for i in range(100000):
            table.hasKey(i)
        end = time.time()
        print(f"Key check: {end - start}s")
        start = time.time()
        for i in range(100000):
            table.remove(i)
        end = time.time()
        print(f"Removal: {end - start}s")
        print("Done.")

    # function to test next prime
    def testNextPrime():
        print("Testing next prime...")
        print('=====================')
        for i in range(1, 100):
            assert DSAHashTable._nextPrime(i) == DSAHashTable._nextPrime(i)
        print("Done.")

    # read csv file into hash table, get rid of duplicates and export to csv
    def testCSV():
        print("Testing CSV...")
        print('==============')
        with open("RandomNames7000.csv", "r") as f:
            table = DSAHashTable.read(f.read())
            #print the table
            for k, v in table:
                print(f"{k},{v}")
        with open("output.csv", "w") as f:
            f.write(table.export())
        print("Done.")

    test()
    benchmark()
    testNextPrime()
    testCSV()
