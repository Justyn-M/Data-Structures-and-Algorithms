#
# DSA Final Assessment Question 3 - Q3BSTree.py
#
# Name : Justyn Mahen
# ID   : 21029112
#
#
import pandas as pd


class Q3BSTree():
    # Inner Treenode class
    class Q2TreeNode():
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    # End inner class

    def __init__(self):
        self.root = None

    def insert(self, val):
        if (self.isEmpty()):
            self.root = self.Q2TreeNode(val)
        else:
            self.root = self.insertRec(val, self.root)

    def isEmpty(self):
        return self.root == None

    def insertRec(self, inVal, cur):
        if (cur == None):
            cur = self.Q2TreeNode(inVal)
        else:
            if (inVal < cur.value):
                cur.left = self.insertRec(inVal, cur.left)
            else:
                cur.right = self.insertRec(inVal, cur.right)
        return cur

# created load factor method
    def getLoadFactor(self):
        return self.getLoadFactorRec(self.root)

    def getLoadFactorRec(self, cur):
        if (cur == None):
            return 0
        else:
            return 1 + self.getLoadFactorRec(cur.left) + self.getLoadFactorRec(cur.right)

# created display methods
    def display(self):
        self.displayRec(self.root)

    def displayRec(self, cur):
        if (cur != None):
            self.displayRec(cur.left)
            print(cur.value)
            self.displayRec(cur.right)

    # Copied some parts of code from what I used in Q3HashTest.py
    def storeMovies(self):
        df = pd.read_csv('6degrees.csv')
        # get the first column, getting rid of duplicate movies and converting to a list which can be stored
        # into the hash table
        df = df.iloc[:, 0]
        df = df.drop_duplicates()
        df = df.values.tolist()
        # creating a new hash table using the length of the df list as the size
        # store the movies into the tree
        tree = Q3BSTree()
        for i in range(0, len(df)):
            tree.insert(df[i])
        # print the tree
        tree.display()
        # load factor
        print("Load Factor is: " + str(tree.getLoadFactor()))

    # Same thing as before but for actors, bits of code borrowed over from Q3HashTest.py as well
    def storeActors(self):
        df = pd.read_csv('6degrees.csv')
        df = df.iloc[:, 3]
        df = df.drop_duplicates()
        df = df.values.tolist()
        tree = Q3BSTree()
        for i in range(0, len(df)):
            tree.insert(df[i])
        tree.display()
        print("Load Factor is: " + str(tree.getLoadFactor()))

    # Once again same thing but now for actor roles
    def storeRoles(self):
        df = pd.read_csv('6degrees.csv')
        df = df.iloc[:, 5]
        df = df.drop_duplicates()
        df = df.values.tolist()
        tree = Q3BSTree()
        for i in range(0, len(df)):
            tree.insert(df[i])
        tree.display()
        print("Load Factor is: " + str(tree.getLoadFactor()))


# code tested in Q3TreeTest.py
