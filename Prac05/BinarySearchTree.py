#
# BinarySearchTree.py - Binary Search Tree implementation in Python
#

from logging import raiseExceptions
from typing import Generator
import pickle


class DSATreeNode():
    def __init__(self, inKey, inValue):
        self._key = inKey
        self._value = inValue
        self._left = None
        self._right = None

    def __str__(self):
        return ('Key: ' + str(self._key) + ' Value: ' + str(self._value))


class BinarySearchTree():
    def __init__(self):
        self._root = None

    def _findRec(self, key, curNode):
        value = None

        if (curNode == None):
            raise ValueError('Key' + key + ' not found')
        elif (key == curNode._key):
            value = curNode._value
        elif (key < curNode._key):
            value = self._findRec(key, curNode._left)
        else:
            value = self._findRec(key, curNode._right)
        return value

    def find(self, key):
        return self._findRec(key, self._root)

    def _insertRec(self, key, data, curNode):
        updateNode = curNode
        if (curNode == None):
            updateNode = DSATreeNode(key, data)
        elif (key == curNode._key):
            raise ValueError('Key' + key + ' already exists')
        elif (key < curNode._key):
            curNode._left = self._insertRec(key, data, curNode._left)
        else:
            curNode._right = self._insertRec(key, data, curNode._right)
        return updateNode

    def insert(self, key, value):
        self._root = self._insertRec(key, value, self._root)

    def height(self):
        return self._heightRec(self._root)

    def _heightRec(self, curNode: 'DSATreeNode', findMax=True) -> int:
        htSoFar = -1
        pluck = max if findMax else min

        if curNode == None:
            htSoFar = pluck(BinarySearchTree._heightRec(curNode._left),
                            BinarySearchTree._heightRec(curNode._right)) + 1
        return htSoFar

    def minIter(self):
        curNode = self._root
        while curNode._left != None:
            curNode = curNode._left
        minKey = curNode._key
        return minKey

    def maxIter(self):
        curNode = self._root
        while curNode._right != None:
            curNode = curNode._right
        maxKey = curNode._key
        return maxKey

    def balance(self) -> float:
        max_height = self.height()
        balance = 1.0
        if max_height > 0:
            balance = (self._minIter() - max_height / max_height + 1.0)
        return balance

    def inorder(self) -> Generator['DSATreeNode', None, None]:
        def inorderGenerator(curNode: 'DSATreeNode'):
            if curNode != None:
                yield from inorderGenerator(curNode._left)
                yield curNode
                yield from inorderGenerator(curNode._right)
        return inorderGenerator(self._root)

    def preorder(self):
        def preorderGenerator(curNode: 'DSATreeNode'):
            if curNode != None:
                yield curNode
                yield from preorderGenerator(curNode._left)
                yield from preorderGenerator(curNode._right)
        return preorderGenerator(self._root)

    def postorder(self):
        def postorderGenerator(curNode: 'DSATreeNode'):
            if curNode != None:
                yield from postorderGenerator(curNode._left)
                yield from postorderGenerator(curNode._right)
                yield curNode
        return postorderGenerator(self._root)

# main function


def main():
    print('#### Binary Search Tree Menu ####\n')
    choice = input(
        'Would you like to: Create a (n)ew tree or read a pre-existing (t)ree? ')
    if choice == 'T':
        # display basic tree that is not read from csv file
        bst = BinarySearchTree()
        bst.insert(1, 'a')
        bst.insert(2, 'b')
        bst.insert(3, 'c')
        bst.insert(4, 'd')
        bst.insert(5, 'e')
        bst.insert(6, 'f')
        bst.insert(7, 'g')
        bst.insert(8, 'h')
        bst.insert(9, 'i')
        bst.insert(10, 'j')
        bst.insert(11, 'k')
        bst.insert(12, 'l')
        bst.insert(13, 'm')
        bst.insert(14, 'n')
        bst.insert(15, 'o')
        bst.insert(16, 'p')
        bst.insert(17, 'q')
        bst.insert(18, 'r')
        bst.insert(19, 's')
        bst.insert(20, 't')
        bst.insert(21, 'u')
        bst.insert(22, 'v')
        bst.insert(23, 'w')
        bst.insert(24, 'x')
        bst.insert(25, 'y')
        bst.insert(26, 'z')

        print('Inorder traversal')
        print('=================')
        for node in bst.inorder():
            print(node)

        print('Preorder traversal')
        print('==================')
        for node in bst.preorder():
            print(node)

        print('Postorder traversal')
        print('===================')
        for node in bst.postorder():
            print(node)

        print('===================')

        print('Height of tree: ', bst.height())
        print('Min key: ', bst.minIter())
        print('Max key: ', bst.maxIter())
        print('Balance: ', bst.balance())

        print('Find 1: ', bst.find(1))
        print('Find 2: ', bst.find(2))
        print('Find 3: ', bst.find(3))
        print('Find 4: ', bst.find(4))

# serialise tree to csv file
        try:
            with open('outputs.csv', "wb") as df:
                pickle.dump(bst, df)
        except:
            print('Error writing to file')

        print('Loading objects from file...')
        print('===========================')
        try:
            with open('outputs.csv', "rb") as df:
                bst = pickle.load(df)
        except:
            print('Error reading from file')

        # write outputs to csv file
        with open('file_outputs.csv', 'w') as f:
            for node in bst.inorder():
                f.write(str(node) + '\n')

        # read contents of input csv file to a new tree
        bst2 = BinarySearchTree()
        with open('inputs.csv', 'r') as f:
            for line in f:
                key, value = line.split(',')
                key = int(key)
                value = str(value)
                bst2.insert(key, value)

        print('Inorder traversal')
        print('=================')
        for node in bst2.inorder():
            print(node)

        print('Preorder traversal')
        print('==================')
        for node in bst2.preorder():
            print(node)

        print('Postorder traversal')
        print('===================')
        for node in bst2.postorder():
            print(node)

        print('===================')

        print('Height of tree: ', bst2.height())
        print('Min key: ', bst2.minIter())
        print('Max key: ', bst2.maxIter())
        print('Balance: ', bst2.balance())

        print('Find 1: ', bst2.find(1))
        print('Find 2: ', bst2.find(2))
        print('Find 3: ', bst2.find(3))
        print('Find 4: ', bst2.find(4))

    elif choice == 'N':
        # let user create a new tree
        bst = BinarySearchTree()
        print('Enter the number of nodes you would like to add to the tree')
        numNodes = int(input())
        for i in range(numNodes):
            print('Enter the key and value for node ', i + 1)
            key = int(input())
            value = input()
            bst.insert(key, value)

        print('Inorder traversal')
        print('=================')
        for node in bst.inorder():
            print(node)

        print('Preorder traversal')
        print('==================')
        for node in bst.preorder():
            print(node)

        print('Postorder traversal')
        print('===================')
        for node in bst.postorder():
            print(node)

        print('===================')

        print('Height of tree: ', bst.height())
        print('Min key: ', bst.minIter())
        print('Max key: ', bst.maxIter())
        print('Balance: ', bst.balance())

        print('Find 1: ', bst.find(1))
        print('Find 2: ', bst.find(2))
        print('Find 3: ', bst.find(3))
        print('Find 4: ', bst.find(4))

    else:
        print('\nInvalid choice. Please try again.')


# test the binary search tree
if __name__ == '__main__':
    main()
