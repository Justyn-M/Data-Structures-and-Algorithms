#
# linkedLists.py - classes for a linked list and list node
#

from logging import raiseExceptions
import pickle


class DSAListNode:
    def __init__(self, data: object, prev: 'DSAListNode', next: 'DSAListNode'):
        self._data = data
        self._prev = prev
        self._next = next


class DSALinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def _insert(self, item: object, after: 'DSAListNode'):
        if after == None:
            # Insert at end
            node = DSAListNode(item, self._tail, None)
            self._tail = node
            if self.isEmpty():
                self._head = node
            else:
                node._prev._next = node
        else:
            node = DSAListNode(item, after._prev, after)
            after._prev = node
            if after is self._head:
                self._head = node
            else:
                node._prev._next = node

    def _remove(self, item: 'DSAListNode') -> object:
        if item is self._head:
            self._head = item._next
        else:
            item._prev.next = item._next

        if item is self._tail:
            self._tail = item._prev
        else:
            item._next._prev = item._prev
        return item._data

    def _find(self, item: object) -> 'DSAListNode':
        node = self._head
        while node != None and item != node._data:
            node = node._next
        return node

    def __iter__(self):
        def forward_gen(iter):
            while iter != None:
                yield iter._data
                iter = iter._next
        return forward_gen(self._head)

    def __reversed__(self):
        def reverse_gen(iter):
            while iter != None:
                yield iter._data
                iter = iter._prev
        return reverse_gen(self._tail)

    def isEmpty(self) -> bool:
        return self._head == None

    def insertFirst(self, item: object):
        self._insert(item, self._head)

    def insertLast(self, item: object):
        self._insert(item, None)

    def insertBefore(self, item: object, before: object):
        self._insert(item, self._find(before))

    def peekFirst(self) -> object:
        return self._head._data

    def peekLast(self) -> object:
        return self._tail._data

    def removeFirst(self) -> object:
        return self._remove(self._head)

    def removeLast(self) -> object:
        return self._remove(self._tail)

    def remove(self, item: object) -> object:
        return self._remove(self._find(item))

    def find(self, item: object) -> bool:
        return self._find(item) != None


# Test code
if __name__ == "__main__":
    list = DSALinkedList()
    list.insertFirst(1)
    list.insertFirst(2)
    list.insertLast(3)
    list.insertLast(4)
    list.insertBefore(5, 3)
    list.remove(3)
    list.removeFirst()
    list.removeLast()
    for item in list:
        print(item)
    for item in reversed(list):
        print(item)

    print(list.find(1))
    print(list.find(2))
    print(list.find(3))
    print(list.find(4))
    print(list.find(5))

    print(list.peekFirst())
    print(list.peekLast())

    print(list.isEmpty())

    list.remove(1)
    print(list.isEmpty())

    print(list.find(1))
    print(list.find(2))
    print(list.find(3))
    print(list.find(4))
    print(list.find(5))

    print(list.peekFirst())
    print(list.peekLast())

    print(list.isEmpty())

    list.insertFirst(1)
    list.insertFirst(2)
    list.insertLast(3)
    list.insertLast(4)
    list.insertBefore(5, 3)
    list.remove(3)
    list.removeFirst()
    list.removeLast()
    for item in list:
        print(item)
    for item in reversed(list):
        print(item)

    print(list.find(1))
    print(list.find(2))
    print(list.find(3))
    print(list.find(4))
    print(list.find(5))

    print(list.peekFirst())
    print(list.peekLast())

    print(list.isEmpty())

    list.remove(1)
    print(list.isEmpty())

    print(list.find(1))
    print(list.find(2))
    print(list.find(3))
    print(list.find(4))
    print(list.find(5))

    print(list.peekFirst())
    print(list.peekLast())

    print(list.isEmpty())

    print('Saving objects to file...')
    print('========================')
    try:
        with open('outputs.txt', "wb") as df:
            pickle.dump(list, df)
    except Exception as e:
        print(e)

    print('Loading objects from file...')
    print('===========================')
    try:
        with open('outputs.txt', "rb") as df:
            list = pickle.load(df)
    except Exception as e:
        print(e)