#
# HashTable.py - DSA hash table implementation
#


class DSAHashTable:
    def __init__(self):
        self.hashdictionary = {}

    def get(self, key):
        return self.hashdictionary[key]

    def put(self, key, value):
        self.hashdictionary[key] = value

    def remove(self, key):
        del self.hashdictionary[key]

    def contains(self, key):
        return key in self.hashdictionary

    def export(self):
        return self.hashdictionary

    def __len__(self):
        return len(self.hashdictionary)

    def __iter__(self):
        return self.hashdictionary.__iter__()

if __name__ == "__main__":
    table = DSAHashTable()
    table.put("one", 1)
    table.put("two", 2)
    table.put("three", 3)

    print(table.get("one"))
    print(table.get("two"))
    print(table.get("three"))

    table.remove("two")
