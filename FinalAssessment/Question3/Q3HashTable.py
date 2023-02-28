#
# DSA Final Assessment Question 3 - Q3HashTable.py
#
# Name : Justyn Mahen
# ID   : 21029112
#
#
import numpy as np
import math
import pandas as pd


class Q3HashTable():
    # Inner class Hash Entry
    class Q3HashEntry():
        # 0 = never used/free,  1 = used / not free

        def __init__(self, inKey="", value=None):
            self.key = inKey
            self.value = value
            if self.key == "":
                self.state = 0
            else:
                self.state = 1
    # End inner class

    def __init__(self, tableSize):

        self.actualSize = self.nextPrime(tableSize - 1)
        self.hashArray = np.zeros(self.actualSize, dtype=object)

        for i in range(0, self.actualSize):
            self.hashArray[i] = self.Q3HashEntry()
        self.hashCount = 0

    def put(self, inKey, inValue):
        hashIdx = self.hash(inKey)
        initIdx = hashIdx
        i = 1

        while (self.hashArray[hashIdx] != None and not self.hashArray[hashIdx].key == inKey):
            if (not self.hashArray[hashIdx].key == inKey):
                if (self.hashArray[hashIdx].state == 1):
                    hashIdx = (initIdx + i) % len(self.hashArray)
                if (self.hashArray[hashIdx].state < 1):
                    self.hashArray[hashIdx] = self.Q3HashEntry(inKey, inValue)
                    self.hashCount = self.hashCount + 1
            i += 1

    def getLoadFactor(self):

        loadFactor = self.hashCount / len(self.hashArray)

        return loadFactor

    def display(self):
        for i in range(0, len(self.hashArray)):
            if (self.hashArray[i].value != None):
                print("\t\t" + str(i) + "\t" + str(self.hashArray[i].key))

    def hash(self, inKey):
        hashIdx = 0
        for i in range(0, len(inKey)):
            hashIdx = hashIdx + ord(inKey[i])
        retVal = hashIdx % len(self.hashArray)
        return retVal

    def nextPrime(self, inNum):

        isPrime = False

        if (inNum % 2 == 0):
            prime = inNum - 1
        else:
            prime = inNum

        while (not isPrime):
            prime = prime + 2
            i = 3
            isPrime = True
            rootVal = math.sqrt(prime)

            while ((i <= rootVal) and (isPrime)):
                if ((prime % i) == 0):
                    isPrime = False
                else:
                    i = i + 2

        return prime

    def getArrayLength(self):
        return len(self.hashArray)

    def get(self, inKey):
        hashIdx = self.hash(inKey)
        initIdx = hashIdx
        i = 1
        while (self.hashArray[hashIdx] != None and not self.hashArray[hashIdx].key == inKey):
            if (not self.hashArray[hashIdx].key == inKey):
                if (self.hashArray[hashIdx].state == 1):
                    hashIdx = (initIdx + i) % len(self.hashArray)
                if (self.hashArray[hashIdx].state < 1):
                    return None
            i += 1
        return self.hashArray[hashIdx].value

    # use pandas to store the first column into the hash table

    def storeMovies(self):
        df = pd.read_csv('6degrees.csv')
        # get the first column, getting rid of duplicate movies and converting to a list which can be stored
        # into the hash table
        df = df.iloc[:, 0]
        df = df.drop_duplicates()
        df = df.values.tolist()
        # creating a new hash table using the length of the df list as the size
        table = Q3HashTable(len(df))
        # storing the values into the hash table
        for i in range(0, len(df)):
            table.put(df[i], df[i])
        table.display()
        # load factor
        print("Load Factor: " + str(table.getLoadFactor()))
        print("### End of Hash Table ###")

    # same thing as storeMovies but for actors
    def storeActors(self):
        df = pd.read_csv('6degrees.csv')
        df = df.iloc[:, 3]
        df = df.drop_duplicates()
        df = df.values.tolist()
        table = Q3HashTable(len(df))
        for i in range(0, len(df)):
            table.put(df[i], df[i])
        table.display()
        print("Load Factor: " + str(table.getLoadFactor()))
        print("### End of Hash Table ###")

# Now its for actor roles
    def storeRoles(self):
        df = pd.read_csv('6degrees.csv')
        df = df.iloc[:, 5]
        df = df.drop_duplicates()
        df = df.values.tolist()
        table = Q3HashTable(len(df))
        for i in range(0, len(df)):
            table.put(df[i], df[i])
        table.display()
        print("Load Factor: " + str(table.getLoadFactor()))
        print("### End of Hash Table ###")

# Testing of these methods are in Q3HashTest.py
